from django import template


def get_status_class(status):
    if status == "Rejected":
        return "fa-circle-xmark text-danger"
    elif status == "Approved":
        return "fa-circle-check text-success"
    else:
        return "fa-circle-minus text-yellow"


register = template.Library()
register.filter('get_status_class', get_status_class)
