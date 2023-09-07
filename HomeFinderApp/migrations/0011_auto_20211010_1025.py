# Generated by Django 3.2.7 on 2021-10-10 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeFinderApp', '0010_auto_20211009_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ac',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='bike',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='fit',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='kids_area',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='modular_kitchen',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='parking_area',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='power_backup',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='refrigerator',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='security',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='tv',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='water',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='balcony',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]