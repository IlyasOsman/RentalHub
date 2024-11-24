# Generated by Django 4.2.11 on 2024-11-24 14:19

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                default="+254", max_length=30, region=None, verbose_name="Phone Number"
            ),
        ),
    ]