# Generated by Django 3.0.14 on 2021-11-12 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fanfics', '0003_remove_publication_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique_for_date=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='fanfics.Publication')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
