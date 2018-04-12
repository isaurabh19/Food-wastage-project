from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf.urls import url
from donationApp.views import DonationFormView, DonationListView, DonationDetailView, SignUpFormView


urlpatterns=[
        #/donate/
        #/donate/thanks
        url(r'^$',auth_views.login,{'template_name':'donationApp/login.html'},name='login'),
        url(r'signup',SignUpFormView.as_view(),name='signup'),
        #url(r'login/,'),
        url(r'donate/',DonationFormView.as_view(),name='donate'),
        url(r'thanks/',TemplateView.as_view(template_name='donationApp/thanks.html'),name='donate-thank-you'),
        url(r'^livefeeds/$',DonationListView.as_view(),name='list-donations'),
        url(r'^livefeeds/(?P<pk>\d+)/$',DonationDetailView.as_view(),name='detail-donations')
]