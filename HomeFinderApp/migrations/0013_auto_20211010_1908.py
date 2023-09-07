# Generated by Django 3.2.7 on 2021-10-10 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeFinderApp', '0012_alter_account_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagefile',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='owner_des',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='owner_imagefile',
            field=models.FileField(blank=True, null=True, upload_to='ProfileImages'),
        ),
        migrations.AlterField(
            model_name='post',
            name='property_des',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='property_id',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='videofile',
            field=models.FileField(blank=True, null=True, upload_to='Videos'),
        ),
    ]
