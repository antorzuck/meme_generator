# Generated by Django 4.1.1 on 2022-09-23 10:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('image', models.ImageField(upload_to='temp')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]