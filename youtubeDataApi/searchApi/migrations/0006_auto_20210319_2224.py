# Generated by Django 3.1.5 on 2021-03-19 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchApi', '0005_merge_20210319_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikeys',
            name='is_active',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
