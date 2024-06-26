# Generated by Django 5.0.3 on 2024-03-31 09:59

import TrendSetter.articles.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TradeIdea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('idea_image', models.ImageField(upload_to='ideas_images/', validators=[TrendSetter.articles.validators.image_size_validator])),
                ('description', models.TextField()),
                ('symbol', models.CharField(max_length=15)),
                ('timeframe', models.CharField(choices=[('short_term', 'Short Term'), ('long_term', 'Long Term')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
