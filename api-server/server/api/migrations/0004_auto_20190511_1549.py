# Generated by Django 2.1.8 on 2019-05-11 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_code_created_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Code',
            new_name='Source',
        ),
    ]