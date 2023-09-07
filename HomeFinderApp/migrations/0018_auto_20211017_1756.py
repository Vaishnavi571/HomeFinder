# Generated by Django 3.2.7 on 2021-10-17 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HomeFinderApp', '0017_propertyimages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertyimages',
            old_name='image',
            new_name='images',
        ),
        migrations.RemoveField(
            model_name='propertyimages',
            name='property_id',
        ),
        migrations.AddField(
            model_name='propertyimages',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='HomeFinderApp.post'),
        ),
    ]
