# Generated by Django 2.2.5 on 2019-09-27 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='engineerregister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('selectgender', models.CharField(max_length=50)),
                ('dateofbirth', models.IntegerField()),
                ('Qualification', models.CharField(max_length=50)),
                ('University', models.CharField(max_length=50)),
                ('uploaddocument', models.FileField(upload_to='')),
                ('workexpierience', models.IntegerField()),
                ('emailid', models.TextField()),
                ('phonenumber', models.IntegerField()),
            ],
        ),
    ]
