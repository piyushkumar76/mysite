# Generated by Django 2.0.2 on 2018-03-08 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180308_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliceEntry',
            fields=[
                ('policeID', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=200)),
                ('PoliceName', models.CharField(max_length=200)),
                ('ForceId', models.CharField(max_length=200, unique=True)),
                ('BatchNo', models.CharField(max_length=200)),
                ('ContactNo', models.CharField(max_length=10)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Stations')),
            ],
        ),
        migrations.RemoveField(
            model_name='policemen',
            name='station',
        ),
        migrations.DeleteModel(
            name='Policemen',
        ),
    ]