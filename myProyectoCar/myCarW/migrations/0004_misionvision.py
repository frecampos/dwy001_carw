# Generated by Django 2.2.16 on 2020-10-08 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCarW', '0003_slidergaleria'),
    ]

    operations = [
        migrations.CreateModel(
            name='MisionVision',
            fields=[
                ('ident', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('mision', models.TextField()),
                ('vision', models.TextField()),
            ],
        ),
    ]
