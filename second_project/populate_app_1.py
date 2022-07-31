import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')
import django
django.setup()

#Fake pop script

import random
from app_1.models import *
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    #get_or_create retrieve topic or create it
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get topic for entry
        top = add_topic()

        #create fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create new webpage entry

        webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]

        acc = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]

        # you need to pass in model object if entry is foreign key

if __name__ == '__main__':
    print("populating script!")
    populate()
    print("Complete!")