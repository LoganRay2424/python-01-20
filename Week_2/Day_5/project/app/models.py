from django.db import models
from datetime import datetime
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validator(self, data):
        errors = {}
        print(data)
        if len(data['first_name'])<2:
            errors['first_name'] = "First name must have 2 and more characters"
        if len(data['last_name'])<2:
            errors['last_name'] = "Last name must have 2 and more characters"
        if data['bday']=="":
            errors['bday']="Birthday cannot be empty"
        else:
            if datetime.today()<datetime.strptime(data['bday'], '%Y-%M-%d'):
                errors['bday']="No dates in the future"
        if not EMAIL_REGEX.match(data['email']):
            errors['email']="Email is invalid"
        if len(data['bio'])>100:
            errors['bio']="Bio too long"
        if data['password']!=data['cpassword']:
            errors['cpass']="Passwords do not match"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    birth_day = models.DateTimeField()
    bio = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()