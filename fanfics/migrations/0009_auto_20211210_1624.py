# Generated by Django 3.0.14 on 2021-12-10 15:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fanfics', '0008_auto_20211124_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='publication_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]