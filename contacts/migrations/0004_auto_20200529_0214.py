# Generated by Django 3.0.5 on 2020-05-29 02:14

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contact_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_1', models.CharField(blank=True, max_length=255, null=True)),
                ('line_2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', localflavor.us.models.USStateField(blank=True, max_length=2, null=True)),
                ('zip_code', localflavor.us.models.USZipCodeField(blank=True, max_length=10, null=True)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('birthday', models.DateField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='favorite_color',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
