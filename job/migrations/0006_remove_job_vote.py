# Generated by Django 2.1.5 on 2020-02-23 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_auto_20200220_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='vote',
        ),
    ]