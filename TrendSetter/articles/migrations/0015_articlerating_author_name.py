# Generated by Django 5.0.3 on 2024-04-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_alter_articlerating_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlerating',
            name='author_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
