from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Gift(models.Model):
    gift = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_who_got_gift = models.ForeignKey(Person, related_name = "gifted", on_delete=models.CASCADE)