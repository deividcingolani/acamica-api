# Generated by Django 3.0.3 on 2020-02-09 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20200209_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type_payment',
            name='dues',
        ),
        migrations.AddField(
            model_name='dues_option',
            name='code',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='dues',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='payments.Dues_Option'),
            preserve_default=False,
        ),
    ]