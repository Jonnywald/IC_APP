import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Desmo_class.settings')

import django
django.setup()

## fake pop script

import random
from first_app.models import AccessRecord,Webpage,Topic,Users
from faker import Faker

fakegen = Faker('pt_BR')
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']
def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        fake_email = fakegen.email()
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
        users = Users.objects.get_or_create(email=fake_email,First_name=fake_first_name,Last_name=fake_last_name)[0]
if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating complete')
