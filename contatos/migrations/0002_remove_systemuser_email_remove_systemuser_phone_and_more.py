# Generated by Django 5.1.2 on 2024-10-25 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemuser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='systemuser',
            name='phone',
        ),
        migrations.AddField(
            model_name='systemuser',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='systemuser',
            name='temp_password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='systemuser',
            name='username',
            field=models.CharField(default=None, max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
