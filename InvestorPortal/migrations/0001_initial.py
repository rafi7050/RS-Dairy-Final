# Generated by Django 3.1.6 on 2021-03-30 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Requester Name')),
                ('nid', models.TextField(max_length=25, verbose_name='NID')),
                ('investor_id', models.TextField(max_length=10, verbose_name='Investor ID')),
                ('phone', models.TextField(max_length=11, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('image', models.ImageField(upload_to=None, verbose_name='Profile Image')),
                ('present_address', models.TextField(max_length=500, verbose_name='Present Address')),
                ('permanent_address', models.TextField(max_length=500, verbose_name='Permanent Address')),
                ('occupation', models.TextField(max_length=100, verbose_name='Occupation')),
                ('total_invest', models.IntegerField()),
                ('own_share', models.IntegerField()),
                ('available_amount', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(max_length=50, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_share', models.CharField(max_length=50)),
                ('available_share', models.IntegerField()),
                ('Per_share_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Share_Rate_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, verbose_name='Requester Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Requester Email')),
                ('cell', models.CharField(max_length=14, verbose_name='Phone Number')),
                ('message', models.TextField(max_length=500, verbose_name='Message')),
                ('sub_text', models.TextField(blank=True, max_length=100, verbose_name='Subject')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='InvestorPortal.investor', verbose_name='Investor')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, verbose_name='Requester Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Requester Email')),
                ('cell', models.CharField(max_length=14, verbose_name='Phone Number')),
                ('message', models.TextField(max_length=500, verbose_name='Message')),
                ('sub_text', models.TextField(blank=True, max_length=100, verbose_name='Subject')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='InvestorPortal.investor', verbose_name='Investor')),
            ],
        ),
        migrations.CreateModel(
            name='Buy_more',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, verbose_name='Requester Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Requester Email')),
                ('cell', models.CharField(max_length=14, verbose_name='Phone Number')),
                ('message', models.TextField(max_length=500, verbose_name='Message')),
                ('sub_text', models.TextField(blank=True, max_length=100, verbose_name='Subject')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='InvestorPortal.investor', verbose_name='Investor')),
            ],
        ),
        migrations.CreateModel(
            name='Account_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('BUY', 'BUY'), ('SELL', 'SELL'), ('WITHDRAW', 'WITHDRAW')], max_length=10, verbose_name='Catagory')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('num_of_share', models.IntegerField(verbose_name='Num Of Share/Withdraw Profit')),
                ('total_amount', models.IntegerField(verbose_name='Total Amount')),
                ('investor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='InvestorPortal.investor')),
            ],
        ),
    ]