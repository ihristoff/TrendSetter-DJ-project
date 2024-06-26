# Generated by Django 5.0.3 on 2024-04-10 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_profile_image_profile_trading_from_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='trading_experience',
            field=models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], default='beginner', max_length=12),
        ),
    ]
