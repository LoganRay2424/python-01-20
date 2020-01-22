from django.db import models
from django.contrib import messages
from datetime import datetime
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data['fname'])<2:
            errors['fname'] = "Name is too short"
        if len(data['lname'])<2:
            errors['lname'] = "Name is too short"
        if not EMAIL_REGEX.match(data['email']):
            errors['email'] = "Email is invalid"
        if len(data['password'])<8:
            errors['password']= "Password needs to be 8 characters or longer"
        if data['password']!=data['cpassword']:
            errors['password'] = "Passwords do not match"
        return errors

class DogManager(models.Manager):
    def validator(self, data):
        errors={}
        if len(data['name'])<2:
            errors['name']="Name has to be longer than 2 characters"
        if data['profile_pic']=="":
            errors['profile']="Must have image url"
        if data['bday']=="":
            errors['bday']="date cannot be empty"
        else:
            if datetime.strptime(data['bday'],'%Y-%M-%d') > datetime.today():
                errors['bday']="No dates in the future"
        if data['age']=="":
            errors['age']="Age cannot be empty"
        if data['weight']=="":
            errors['weight']="Weight cannot be empty"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Dog(models.Model):
    name = models.CharField(max_length=60)
    profile_pic_url = models.TextField()
    bio = models.TextField()
    age = models.IntegerField()
    weight = models.IntegerField()
    is_good_boy = models.BooleanField(default=False)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DogManager()

    submitted_by = models.ForeignKey(
        'User', on_delete='CASCADE', related_name="dogs"
    )

    tricks = models.ManyToManyField("Trick", related_name="dogs_with_tricks")


class Trick(models.Model):
    name = models.CharField(max_length=100)