# Generated by Django 2.2.5 on 2019-10-14 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0005_auto_20191014_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerregistration',
            name='emailid',
            field=models.EmailField(default='k@gmail.com', max_length=50),
        ),
    ]
