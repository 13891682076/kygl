# Generated by Django 2.1.7 on 2019-12-09 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20190523_1503'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-created_at',), 'verbose_name': '新闻', 'verbose_name_plural': '新闻'},
        ),
    ]
