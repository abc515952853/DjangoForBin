# Generated by Django 3.0.3 on 2020-02-25 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='sex',
            field=models.CharField(default='男', max_length=19),
        ),
    ]