# Generated by Django 4.2.11 on 2024-04-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fest_app', '0017_customuser_catwalk_customuser_duodance_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='reel',
            new_name='rell',
        ),
        migrations.AddField(
            model_name='customuser',
            name='college_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
