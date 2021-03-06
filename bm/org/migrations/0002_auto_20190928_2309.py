# Generated by Django 2.2.5 on 2019-09-28 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='farmerregistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name1', models.CharField(max_length=50)),
                ('Name2', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('options', models.CharField(max_length=50)),
                ('idnumber', models.TextField()),
                ('address', models.TextField()),
                ('pincode', models.IntegerField()),
                ('phonenumber', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='engineerregister',
            name='uploaddocument',
        ),
        migrations.AlterField(
            model_name='engineerregister',
            name='dateofbirth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='engineerregister',
            name='emailid',
            field=models.CharField(max_length=50),
        ),
    ]
