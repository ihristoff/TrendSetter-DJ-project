# Generated by Django 5.0.3 on 2024-03-27 12:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='trading_from',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='trendsetteruser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'A user with that email already exists'}, max_length=50, unique=True),
        ),
    ]
