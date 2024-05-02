from django import template
from myapp.models import Request

register = template.Library()

@register.filter
def is_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

@register.filter
def already_requested(current_patient, doctor):
    return Request.objects.filter(sender=current_patient, receiver=doctor).exists()