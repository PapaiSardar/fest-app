# Generated by Django 5.0.1 on 2024-03-13 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fest_app', '0008_events_detalis_delete_event_det_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_detalis',
            name='id_card',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student_detalis',
            name='payment_ss',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
