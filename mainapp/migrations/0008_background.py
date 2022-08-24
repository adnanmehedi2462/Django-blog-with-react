# Generated by Django 4.0.5 on 2022-08-03 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_profile_about_alter_profile_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='bg_image')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]