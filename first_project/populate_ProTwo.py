import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# FAKE POP SCRIPTS

import random
from ProTwo.models import User
from faker import Faker

fakegenerator = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fakegenerator.first_name()
        fake_lname = fakegenerator.last_name()
        fake_email = fakegenerator.email()

        userinfo = User.objects.get_or_create(FirstName=fake_name, LastName=fake_lname, Email=fake_email)[0]
        userinfo.save()


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
