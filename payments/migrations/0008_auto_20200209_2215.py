# Generated by Django 3.0.3 on 2020-02-09 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_auto_20200209_2213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='Student',
            new_name='student',
        ),
    ]
