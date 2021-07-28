# Generated by Django 3.2.5 on 2021-07-24 11:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0015_auto_20210724_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('room_id', models.AutoField(max_length=10, primary_key=True, serialize=False, verbose_name='ルームID')),
                ('user_id', models.CharField(max_length=10, verbose_name='ユーザーID')),
                ('partner_user_id', models.CharField(max_length=10, verbose_name='会話相手ユーザーID')),
                ('chat', models.CharField(max_length=170, verbose_name='会話内容')),
                ('delete_flg', models.BooleanField(null=True, verbose_name='削除フラグ')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日時')),
                ('delete_date', models.DateTimeField(null=True, verbose_name='削除日時')),
            ],
        ),
    ]
