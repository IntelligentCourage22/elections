from polls.models import Choice, Poll, Vote
from django.contrib.auth.models import User
import datetime
import random
import time
from faker import Faker
import string
fake = Faker()


'''Aadya  - NZSOZ8
 Aarush  - 0T8VEI
 Aathreya  - O31BS7
 Akanksha  - 628TZW
 Amod  - K816J2U  
 Amrit  - H7LKNH  
 Anikethan  - QN8IXM  
 Ankit  - QT7QPX  
 Anshula  - 51KZGS  
 Atulya - 0DWB3V  
 Daniel  - PWZO9V  
 Dharshita  - M5MBND  
 Dhruv - D1R13L  
 Harshita  - VVAT1B  
 Jeevika - BKBUGF  
 Kenisha  - YA5PBG  
 Lekshmi  - DUOQGY  
 Manushree  - 3NGFFV  
 Meghali  - 2HURHU  
 Meghana  - VXWRCC  
 Mithil  - MET72N
 Harshith  - P1V7N3  
 Navya  - 8WV9GY  
 Nihaar - BCR49L  
 Nishanth  - 3D037I  
 Preryth  - MTB27Y  
 Riddhima  - E7A2AK
 Vaibhavi - 8RHWQL  
 Siddarth - DQ7N29  
 Sohani  - VE6E63  
 Swasti  - X8T0HK  
 Tanya  - Y7FBOB  
 Yeshas - GG4078'''


ss = '''Aadya
Aarush
Aathreya
Akanksha
Amod
Amrit
Anikethan
Ankit
Anshula
Atulya
Daniel
Dharshita
Dhruv
Harshita
Jeevika
Kenisha
Lekshmi
Manushree
Meghali
Meghana
Mithil
Harshith
Navya
Nihaar
Nishanth
Preryth
Riddhima
Vaibhavi
Siddarth
Sohani
Swasti
Tanya
Yeshas'''

li = list(ss.split("\n"))


def seed_users(num_entries=len(li), overwrite=True):
    """
    Creates num_entries worth a new users
    """
    if overwrite:
        print("Overwriting Users")
        User.objects.all().delete()
    count = 0
    for i in range(0, num_entries-1):
        first_name = fake.first_name()
        last_name = fake.last_name()
        username = li[i]
        password = username + "".join(random.choices(string.ascii_uppercase +
                                                     string.digits, k=3))
        u = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=first_name + "." + last_name + "@mail.com",
            username=username,
            password=password
        )
        count += 1
        percent_complete = count / num_entries * 100
        print(f"{username} - {password}")

        # print(
        #    "Adding {} new Users: {:.2f}%".format(
        #        num_entries, percent_complete),
        #    end='\r',
        #    flush=True
        # )
    print()

    '''if overwrite:
        print("Overwriting Users")
        User.objects.all().delete()
    count = 0
    for _ in range(num_entries):
        first_name = fake.first_name()
        last_name = fake.last_name()
        u = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=first_name + "." + last_name + "@fakermail.com",
            username=first_name + last_name,
            password="password"
        )
        count += 1
        percent_complete = count / num_entries * 100
        print(
            "Adding {} new Users: {:.2f}%".format(
                num_entries, percent_complete),
            end='\r',
            flush=True
        )
    print()'''


def seed_polls(num_entries=10, choice_min=2, choice_max=5, overwrite=False):

    if overwrite:
        print('Overwriting polls')
        Poll.objects.all().delete()
    users = list(User.objects.all())
    count = 0
    for _ in range(num_entries):
        p = Poll(
            owner=random.choice(users),
            text=fake.paragraph(),
            pub_date=datetime.datetime.now()
        )
        p.save()
        num_choices = random.randrange(choice_min, choice_max + 1)
        for _ in range(num_choices):
            c = Choice(
                poll=p,
                choice_text=fake.sentence()
            ).save()
        count += 1
        percent_complete = count / num_entries * 100
        print(
            "Adding {} new Polls: {:.2f}%".format(
                num_entries, percent_complete),
            end='\r',
            flush=True
        )
    print()


def seed_votes():

    Vote.objects.all().delete()
    users = User.objects.all()
    polls = Poll.objects.all()
    count = 0
    number_of_new_votes = users.count() * polls.count()
    for poll in polls:
        choices = list(poll.choice_set.all())
        for user in users:
            v = Vote(
                user=user,
                poll=poll,
                choice=random.choice(choices)
            ).save()
            count += 1
            percent_complete = count / number_of_new_votes * 100
            print(
                "Adding {} new votes: {:.2f}%".format(
                    number_of_new_votes, percent_complete),
                end='\r',
                flush=True
            )
    print()


def seed_all(num_entries=10, overwrite=False):
 
    start_time = time.time()
    # run seeds
    seed_users(num_entries=num_entries, overwrite=overwrite)
    seed_polls(num_entries=num_entries, overwrite=overwrite)
    seed_votes()
    # get time
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print("Script Execution took: {} minutes {} seconds".format(minutes, seconds))
