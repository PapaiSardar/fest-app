# Generated by Django 4.2.11 on 2024-04-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fest_app', '0016_customuser_id_card_image_customuser_roll_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='catwalk',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='duodance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='facepaint',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='reel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='selfie',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='twomintofame',
            field=models.BooleanField(default=False),
        ),
    ]
