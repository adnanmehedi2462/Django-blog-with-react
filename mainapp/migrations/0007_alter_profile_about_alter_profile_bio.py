# Generated by Django 4.0.5 on 2022-07-21 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_remove_post_created_at_remove_post_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, default='About Empty..!!', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, default='Bio Empty..!!', max_length=400, null=True),
        ),
    ]
