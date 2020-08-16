from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #people - the people that this user has saved dates for

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    desc = models.TextField(default="")
    p_type = models.CharField(max_length=4, default="")
    user = models.ForeignKey(User, related_name='people', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #gifts - the important dates that are aligned with this person
    def sum_gift_money(self):
        sum = 0
        all_gifts = self.gifts.all()
        for gift in all_gifts:
            sum = sum + gift.money 
        return sum

class Gift(models.Model):
    date = models.DateField()
    date_name = models.CharField(max_length=255)
    gift = models.CharField(max_length=255)
    note = models.TextField(default='')
    money = models.DecimalField(max_digits=10, decimal_places=2)
    person = models.ForeignKey(Person, related_name='gifts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)