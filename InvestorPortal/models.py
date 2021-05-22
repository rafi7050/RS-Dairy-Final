from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Investor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="Requester Name")
    nid = models.TextField(max_length=25, verbose_name="NID")
    investor_id = models.TextField(max_length=10, verbose_name="Investor ID")
    phone = models.TextField(max_length=11, verbose_name="Phone")
    email = models.EmailField(verbose_name="Email")
    image = models.ImageField(upload_to=None, verbose_name="Profile Image")
    present_address = models.TextField(max_length=500, verbose_name="Present Address")
    permanent_address = models.TextField(max_length=500, verbose_name="Permanent Address")
    occupation = models.TextField(max_length=100, verbose_name="Occupation")
    total_invest = models.IntegerField()
    own_share = models.IntegerField()
    available_amount = models.IntegerField()



    def __str__(self):
        return self.name


class Issue(models.Model):
    name = models.TextField(max_length=50, verbose_name="Requester Name")
    email = models.EmailField(verbose_name="Requester Email")
    cell = models.CharField(max_length=14, verbose_name="Phone Number")
    message = models.TextField(max_length=500, verbose_name="Message")
    sub_text = models.TextField(max_length=100, blank=True, verbose_name="Subject")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Investor, on_delete=models.CASCADE, default=False, verbose_name="Investor")

    def __str__(self):
        return self.email


class Buy_more(models.Model):
    name = models.TextField(max_length=50, verbose_name="Requester Name")
    email = models.EmailField(verbose_name="Requester Email")
    cell = models.CharField(max_length=14, verbose_name="Phone Number")
    message = models.TextField(max_length=500, verbose_name="Message")
    sub_text = models.TextField(max_length=100, blank=True, verbose_name="Subject")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Investor, on_delete=models.CASCADE, default=False, verbose_name="Investor")

    def __str__(self):
        return self.email


class Withdraw(models.Model):
    name = models.TextField(max_length=50, verbose_name="Requester Name")
    email = models.EmailField(verbose_name="Requester Email")
    cell = models.CharField(max_length=14, verbose_name="Phone Number")
    message = models.TextField(max_length=500, verbose_name="Message")
    sub_text = models.TextField(max_length=100, blank=True, verbose_name="Subject")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Investor, on_delete=models.CASCADE, default=False, verbose_name="Investor")

    def __str__(self):
        return self.email


class Share(models.Model):
    total_share = models.CharField(max_length=50)
    available_share = models.IntegerField()
    Per_share_amount = models.IntegerField()


class Notice(models.Model):
    title = models.TextField(max_length=50, verbose_name="Title")
    description = models.TextField(max_length=50, verbose_name="Description")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Share_Rate_history(models.Model):
    date = models.DateField(verbose_name="Date")
    price = models.IntegerField()

    def __str__(self):
        return f'{self.date}'
CATEGORY_CHOICES = (
    ('BUY', 'BUY'),
    ('SELL', 'SELL'),
    ('WITHDRAW', 'WITHDRAW')
 
)

class  Account_history(models.Model):
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE,default=None)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10,verbose_name='Catagory')
    created_at = models.DateTimeField(auto_now=True)
    num_of_share=models.IntegerField(verbose_name='Num Of Share/Withdraw Profit')
    total_amount=models.IntegerField(verbose_name='Total Amount')


    def __str__(self):
        return self.category
    
