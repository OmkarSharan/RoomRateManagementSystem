# Generated by Django 4.2.15 on 2024-09-04 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomrates', '0002_remove_discount_id_remove_roomrate_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomrate',
            old_name='room_id',
            new_name='room_ids',
        ),
    ]
