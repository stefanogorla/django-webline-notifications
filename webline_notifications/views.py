from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils import timezone
from webline_notifications.models import Notification
from django.http import HttpResponse, HttpResponseForbidden

custom_view = getattr(settings, 'WEBLINE_NOTIFICATIONS_CUSTOM_VIEW', False)

@login_required
def see_all_notification(request):
    if request.is_ajax():
        Notification.seen_all(request.user)
        return HttpResponse()
    else:
        return HttpResponseForbidden('<h1>Forbidden</h1>you cant use this url in this way')


@login_required
def dispatch_url(request, notification_id):
    try:
        n = Notification.objects.get(pk=notification_id)
        n.seen_date = timezone.now()
        n.save()
        if n.url:
            return redirect(n.url)
    except:
        pass
    if custom_view:
        return redirect(custom_view)
    return redirect('admin:webline_notifications_notification_changelist')
