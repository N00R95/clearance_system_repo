from django.core.management.base import BaseCommand
from django.utils.text import slugify

from core.constants import departments
from core.models import Department, User


def to_camel_case(text):
    splited = text.split('_')
    return ' '.join(x.title() for x in splited)


def create_users():
    departments_to_create = Department.objects.all()
    for department in departments_to_create:
        User.objects.create_superuser(username=slugify(department.name_en), password="0000", department=department)
    hr_department = Department.objects.get(name_en="Human Resources")
    User.objects.create_superuser(username='admin', password="0000", department=hr_department)


def create_departments():
    for sector in departments:
        parent_department = sector["parent_department"]
        ar_departments = sector["ar_department"]
        en_departments = sector["en_department"]
        hidden = sector.get("hidden", False)
        for ar_department, en_department in zip(ar_departments, en_departments):
            Department.objects.create(parent_department=to_camel_case(parent_department),
                                      name_ar=ar_department,
                                      name_en=to_camel_case(en_department), hidden=hidden)


class Command(BaseCommand):
    help = 'Seed the whole system'

    def handle(self, *args, **options):
        create_departments()
        create_users()
