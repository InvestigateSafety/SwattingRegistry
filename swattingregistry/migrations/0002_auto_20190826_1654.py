# Generated by Django 2.2.4 on 2019-08-26 16:54

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swattingregistry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='concerns',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='name2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='household',
            name='name3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='household',
            name='phone2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='household',
            name='phone3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='household',
            name='place_details',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='streaming_url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
