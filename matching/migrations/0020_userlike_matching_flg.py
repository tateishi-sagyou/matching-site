# Generated by Django 3.2.5 on 2021-07-26 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0019_auto_20210724_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlike',
            name='matching_flg',
            field=models.BooleanField(default=False, null=True, verbose_name='マッチングフラグ'),
        ),
    ]
