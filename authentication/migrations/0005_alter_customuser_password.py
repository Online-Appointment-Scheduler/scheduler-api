# Generated by Django 4.2.4 on 2023-08-24 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_customuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(default=' ', max_length=128, null=True),
        ),
    ]
