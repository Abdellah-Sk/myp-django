# Generated by Django 3.1.1 on 2020-10-13 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20201013_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='github',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]