# Generated by Django 3.0.5 on 2020-05-29 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20200529_0214'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='species',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
