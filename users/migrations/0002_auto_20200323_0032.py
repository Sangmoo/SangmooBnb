# Generated by Django 2.2.5 on 2020-03-22 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user", old_name="language", new_name="language",
        ),
    ]
