# Generated by Django 2.0.3 on 2018-05-09 04:07

from django.db import migrations, models
import zp.models


class Migration(migrations.Migration):

    dependencies = [
        ('zp', '0007_auto_20180509_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate1',
            name='dp',
            field=models.ImageField(null=True, upload_to=zp.models.upload_image),
        ),
    ]
