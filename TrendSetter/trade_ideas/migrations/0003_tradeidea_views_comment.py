# Generated by Django 5.0.3 on 2024-04-12 10:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_ideas', '0002_tradeidea_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tradeidea',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='idea_comments', to=settings.AUTH_USER_MODEL)),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trade_ideas.tradeidea')),
            ],
        ),
    ]
