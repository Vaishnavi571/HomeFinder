# Generated by Django 3.2.7 on 2021-10-13 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HomeFinderApp', '0013_auto_20211010_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imagefile',
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Images', verbose_name='Image')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='HomeFinderApp.post')),
            ],
        ),
    ]
