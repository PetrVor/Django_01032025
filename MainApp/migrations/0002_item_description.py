# Generated by Django 5.1.6 on 2025-03-10 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='Base item description', max_length=200),
        ),
    ]
