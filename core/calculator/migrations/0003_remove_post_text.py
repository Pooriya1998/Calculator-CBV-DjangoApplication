# Generated by Django 3.2.20 on 2023-09-02 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_auto_20230902_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
    ]
