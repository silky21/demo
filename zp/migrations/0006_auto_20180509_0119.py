# Generated by Django 2.0.3 on 2018-05-08 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zp', '0005_auto_20180507_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate1',
            name='image',
            field=models.ImageField(null=True, upload_to='zp/static/pic_folder/'),
        ),
        migrations.AddField(
            model_name='donate1',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
