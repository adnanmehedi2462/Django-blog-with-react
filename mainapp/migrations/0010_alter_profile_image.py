# Generated by Django 4.0.5 on 2022-08-06 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_alter_background_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='User_image'),
        ),
    ]
