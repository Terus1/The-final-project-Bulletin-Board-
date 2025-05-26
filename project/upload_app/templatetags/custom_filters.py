from django import template


register = template.Library()


@register.filter(name='strip_p')
def strip_p(value):
    return value.replace('<p>', '').replace('</p>', '').replace('<br>', '')

