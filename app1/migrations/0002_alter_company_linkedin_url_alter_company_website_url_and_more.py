# Generated by Django 5.1 on 2024-09-20 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='linkedin_url',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='website_url',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='founder',
            name='linkedin_url',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='linkedin_url',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='linkedin_url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
