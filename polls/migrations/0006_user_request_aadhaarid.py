# Generated by Django 2.0.2 on 2018-04-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20180409_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_request',
            name='AadhaarID',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
