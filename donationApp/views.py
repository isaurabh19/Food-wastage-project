from django.forms.formsets import formset_factory
from django.views.generic.edit import CreateView,FormView
from .models import UserModel
from forms import DonorDetailsForm,FoodItemForm
import logging

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)
logger.info("success")
# Create your views here.
class DonationFormView(FormView):
    template_name = 'donationApp/donate_form.html'
    form_class = DonorDetailsForm
    logger.info("form view success")
    def get_form_kwargs(self):
        logger.info('called get form kwargs')
        kwargs=super(DonationFormView,self).get_form_kwargs()
        try:
            user=UserModel.objects.get(email=self.request.user.email)
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
        FoodItemFormset=formset_factory(FoodItemForm,extra=1)
        food_formset=FoodItemFormset()
        context['food_formset']=food_formset
        return context

    def post(self, request, *args, **kwargs):
        pass
