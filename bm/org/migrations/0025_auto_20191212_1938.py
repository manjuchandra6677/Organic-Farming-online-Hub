# Generated by Django 2.2.5 on 2019-12-12 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0024_auto_20191212_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='typesofcrops',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='typesofcrops',
            name='season',
            field=models.CharField(default='', max_length=50),
        ),
    ]
