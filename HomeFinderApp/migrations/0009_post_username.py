# Generated by Django 3.2.7 on 2021-10-06 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HomeFinderApp', '0008_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeFinderApp.account'),
        ),
    ]
