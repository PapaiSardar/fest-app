# Generated by Django 4.2.11 on 2024-05-07 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fest_app', '0023_catwalkteam_catwalkteammember_delete_eventtotals'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catwalkteam',
            name='leader',
        ),
        migrations.AddField(
            model_name='catwalkteam',
            name='leader_roll_number',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
