# Generated by Django 4.2.4 on 2023-08-24 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_customuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(default='password', max_length=128, null=True),
        ),
    ]
