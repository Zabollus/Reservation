# Generated by Django 4.0.6 on 2022-07-13 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservationapp', '0002_alter_room_name_reservation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='room_id',
            new_name='room',
        ),
    ]