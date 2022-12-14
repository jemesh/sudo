# Generated by Django 4.1.3 on 2022-11-23 05:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_usermodel_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='mobile',
            field=models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+99-0123456789'.", regex='^\\+?1?\\d{9,11}$')]),
        ),
    ]
