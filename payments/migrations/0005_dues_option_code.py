# Generated by Django 3.0.3 on 2020-02-09 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_remove_dues_option_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='dues_option',
            name='code',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
