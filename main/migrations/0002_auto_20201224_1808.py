# Generated by Django 3.1.2 on 2020-12-24 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advuser',
            old_name='send_message',
            new_name='send_messages',
        ),
    ]