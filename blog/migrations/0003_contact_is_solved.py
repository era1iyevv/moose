# Generated by Django 4.2.9 on 2024-02-06 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_solved',
            field=models.BooleanField(default=False),
        ),
    ]
