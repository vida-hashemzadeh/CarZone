# Generated by Django 3.0.7 on 2021-03-08 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='disignation',
            new_name='designation',
        ),
    ]
