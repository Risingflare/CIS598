# Generated by Django 2.2.6 on 2019-11-19 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storetransfer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributor',
            name='distributor_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
