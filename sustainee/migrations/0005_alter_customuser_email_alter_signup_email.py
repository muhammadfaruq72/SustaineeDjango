# Generated by Django 4.1.3 on 2022-12-09 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sustainee', '0004_alter_customuser_email_delete_refreshtoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
