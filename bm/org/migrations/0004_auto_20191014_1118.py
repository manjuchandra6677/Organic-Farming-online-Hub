# Generated by Django 2.2.5 on 2019-10-14 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0003_signin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='signin',
        ),
        migrations.AddField(
            model_name='farmerregistration',
            name='emailid',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
