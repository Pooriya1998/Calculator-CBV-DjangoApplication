# Generated by Django 3.2.20 on 2023-09-02 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='history_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='history_title',
            new_name='title',
        ),
    ]
