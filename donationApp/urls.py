from django.views.generic.base import TemplateView
from django.conf.urls import url
from django.urls import reverse_lazy
from donationApp.views import DonationFormView, DonationListView, DonationDetailView, SignUpFormView
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
        #/donate/
        #/donate/thanks
        url(r'^$',TemplateView.as_view(template_name='donationApp/home.html'),name='home'),
        url(r'signup',SignUpFormView.as_view(),name='signup'),
        url(r'login',LoginView.as_view(template_name='donationApp/login.html'),name='login'),
        url(r'logout',LogoutView.as_view(next_page=reverse_lazy('login')),name='logout'),
        url(r'donate',DonationFormView.as_view(),name='donate'),
        url(r'thanks',TemplateView.as_view(template_name='donationApp/thanks.html'),name='donate-thank-you'),
        url(r'^livefeeds/$',DonationListView.as_view(),name='list-donations'),
        url(r'^livefeeds/(?P<pk>\d+)/$',DonationDetailView.as_view(),name='detail-donations')
]