# Generated by Django 4.2.15 on 2024-08-30 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomrates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='id',
        ),
        migrations.RemoveField(
            model_name='roomrate',
            name='id',
        ),
        migrations.AlterField(
            model_name='discount',
            name='discount_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='roomrate',
            name='room_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
