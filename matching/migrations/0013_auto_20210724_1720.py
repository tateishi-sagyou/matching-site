# Generated by Django 3.2.5 on 2021-07-24 08:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0012_auto_20210724_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='userimage',
            name='delete_date',
            field=models.DateTimeField(null=True, verbose_name='削除日時'),
        ),
        migrations.AddField(
            model_name='userimage',
            name='delete_flg',
            field=models.BooleanField(null=True, verbose_name='削除フラグ'),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='user_images',
            field=models.ImageField(upload_to='image/', verbose_name='イメージ'),
        ),
    ]