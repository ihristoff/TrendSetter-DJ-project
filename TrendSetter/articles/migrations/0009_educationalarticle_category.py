# Generated by Django 5.0.3 on 2024-04-15 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_rename_rating_articlerating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationalarticle',
            name='category',
            field=models.CharField(choices=[('Chart patterns', 'Chart patterns'), ('Trendlines', 'Trendlines'), ('Candlesticks', 'Candlesticks'), ('Supply and Demand', 'Supply and Demand'), ('Elliott Wave Theory', 'Elliott Wave Theory'), ('Volume Analysis', 'Volume Analysis'), ('Other', 'Other')], default='Other', max_length=25),
        ),
    ]
