# Generated by Django 4.1.3 on 2022-11-23 05:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_customer_alter_usermodel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='mobile',
            field=models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
