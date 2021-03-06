# Generated by Django 3.2.5 on 2021-07-24 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0009_alter_userimage_user_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userimage',
            old_name='reated_date',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='user',
            name='delete_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='delete_flg',
            field=models.BooleanField(null=True),
        ),
    ]
