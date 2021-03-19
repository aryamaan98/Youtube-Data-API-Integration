# Generated by Django 3.1.5 on 2021-03-19 21:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('searchApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiKeys',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('api_key', models.TextField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]