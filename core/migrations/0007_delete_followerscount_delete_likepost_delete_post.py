# Generated by Django 5.0.2 on 2024-03-19 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_post_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FollowersCount',
        ),
        migrations.DeleteModel(
            name='LikePost',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
