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
####
#Aadya  - NZSOZ8
# Aarush  - 0T8VEI: 3.03%
# Aathreya  - O31BS7: 6.06%
# Akanksha  - 628TZW: 9.09%
# Amod  - K816J2U: 12.12%
# Amrit  - H7LKNH: 15.15%
# Anikethan  - QN8IXM: 18.18%
# Ankit  - QT7QPX: 21.21%
# Anshula  - 51KZGS: 24.24%
# Atulya - 0DWB3V: 27.27%
# Daniel  - PWZO9V: 30.30%
# Dharshita  - M5MBND: 33.33%
# Dhruv - D1R13L: 36.36%
# Harshita  - VVAT1B: 39.39%
# Jeevika - BKBUGF: 42.42%
# Kenisha  - YA5PBG: 45.45%
# Lekshmi  - DUOQGY: 48.48%
# Manushree  - 3NGFFV: 51.52%
# Meghali  - 2HURHU: 54.55%
# Meghana  - VXWRCC: 57.58%
# Mithil  - MET72N: 60.61%
# Harshith  - P1V7N3: 63.64%
# Navya  - 8WV9GY: 66.67%
# Nihaar - BCR49L: 69.70%
# Nishanth  - 3D037I: 72.73%
# Preryth  - MTB27Y: 75.76%
# Riddhima  - E7A2AK: 78.79%
# Vaibhavi - 8RHWQL: 81.82%
# Siddarth - DQ7N29: 84.85%
# Sohani  - VE6E63: 87.88%
# Swasti  - X8T0HK: 90.91%
# Tanya  - Y7FBOB: 93.94%
# Yeshas - GG4078
####

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
Yeshas '''

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
        password = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=6))

        username = li[i]
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

        print(
            "Adding {} new Users: {:.2f}%".format(
                num_entries, percent_complete),
            end='\r',
            flush=True
        )
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
    """
    Seeds num_entries poll with random users as owners
    Each poll will be seeded with # choices from choice_min to choice_max
    """
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
    """
    Creates a new vote on every poll for every user
    Voted for choice is selected random.   
    Deletes all votes prior to adding new ones
    """
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
    """
    Runs all seeder functions. Passes value of overwrite to all
    seeder function calls.
    """
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
