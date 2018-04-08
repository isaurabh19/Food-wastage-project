import logging

from django.core.mail import EmailMessage
from django.forms.formsets import formset_factory
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from forms import DonorDetailsForm, FoodItemForm, SignUpForm
from .models import UserModel, DonationModel
from django.contrib.auth import authenticate,login
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger(__name__)

# Create your views here.
class DonationListView(ListView):
    queryset = DonationModel.objects.filter(receiver='')
    template_name = 'donationApp/donation_list.html'

class DonationDetailView(LoginRequiredMixin,DetailView):
    model = DonationModel
    template_name = 'donationApp/donation_detail.html'
    login_url='/login/'

class SignUpFormView(FormView):
    template_name = 'donationApp/signup.html'
    form_class = SignUpForm
    success_url = '/thanks/'

    def post(self, request, *args, **kwargs):
        form=SignUpForm(request.POST)
        logger.debug("here in post of form")
        if form.is_valid():
            form.save()
            #logger.info(user.email+'signed up')
            username=form.cleaned_data['email']
            password=form.cleaned_data['password1']
            u=authenticate(request,username=username,password=password)
            login(request,u)
            return self.form_valid(form)
        else:
            logger.info(form)
            return self.form_invalid(form)


class DonationFormView(FormView):
    template_name = 'donationApp/donate_form.html'
    form_class = DonorDetailsForm
    success_url = '/thanks/'
#TODO CHANGE USERMODEL WITH CUSTOMUSERAUTHMODEL
    def get_form_kwargs(self):
        logger.info('called get form kwargs')
        kwargs=super(DonationFormView,self).get_form_kwargs()
        try:
            user=self.request.user
            kwargs['user']=user
        except:
            #object does not exist
            raise
        return kwargs

    def get_context_data(self, **kwargs):
        logger.info('called get context')
        context=super(DonationFormView,self).get_context_data()
        form=self.get_form(self.form_class)
        context['form']=form
        FoodItemFormset=formset_factory(FoodItemForm,extra=1, can_delete=True)
        food_formset=FoodItemFormset()
        context['food_formset']=food_formset
        return context

    def post(self, request, *args, **kwargs):
        user = UserModel.objects.get(email=request.user.email)
        logger.info(user)
        donation=DonationModel()
        donor_form= DonorDetailsForm(request.POST,user=user)
        FoodItemFormset=formset_factory(FoodItemForm)
        fooditem_formset=FoodItemFormset(request.POST)

        if donor_form.is_valid() and fooditem_formset.is_valid():
            donation.donor=donor_form.cleaned_data.get('donor_name')
            donation.donor_address=donor_form.cleaned_data.get('donor_address')
            donation.donor_email=user.email
            donation.donor_contact=donor_form.cleaned_data.get('donor_contact')

            food_items={}
            for forms in fooditem_formset:
                food_items[forms.cleaned_data.get('food_name')]=forms.cleaned_data.get('food_quantity')

            donation.donation_items=food_items
            donation.save()

            return self.form_valid(donor_form,donation)

    def form_valid(self, form,donation_object):
        e=EmailMessage()
        e.subject="New Donation Made!"
        e.body="View the detailed donation from {} here: {}".format(form.donor,donation_object.get_absolute_url())
        e.to=UserModel.objects.filter(is_receiver=True)
        e.send()
        return super(DonationFormView, self).form_valid(form)


