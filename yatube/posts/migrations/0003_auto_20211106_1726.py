# Generated by Django 2.2.19 on 2021-11-06 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20211106_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='slugs',
            new_name='slug',
        ),
    ]