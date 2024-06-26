# Generated by Django 5.0.3 on 2024-04-18 18:08

import TrendSetter.articles.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_profile_show_email_alter_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/', validators=[TrendSetter.articles.validators.image_size_validator]),
        ),
    ]
