from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^see-all/$',
        views.see_all_notification, name='see_all_notification'),
    url(r'^dispatch/(?P<notification_id>[0-9]+)/$',
        views.dispatch_url, name='dispatch_url'),
]