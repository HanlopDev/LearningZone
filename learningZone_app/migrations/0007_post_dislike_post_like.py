# Generated by Django 4.0.4 on 2022-05-21 10:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learningZone_app', '0006_alter_userprofile_bio_alter_userprofile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislike',
            field=models.ManyToManyField(blank=True, related_name='dislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
