from atexit import register
from multiprocessing import context
from django import template
from learningZone_app.models import Notificatons

register = template.Library()

@register.inclusion_tag('learningZone_app/show_notifications.html', takes_context=True)
def show_notifications(context):
    request_user = context['request'].user
    notifications = Notificatons.objects.filter(to_user=request_user).exclude(user_has_seen=True).order_by('-date')
    return {'notifications': notifications}