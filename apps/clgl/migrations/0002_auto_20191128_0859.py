# Generated by Django 2.1.7 on 2019-11-28 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clgl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
    ]
