# Generated by Django 4.0.6 on 2022-07-24 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Room',
            new_name='Post',
        ),
    ]