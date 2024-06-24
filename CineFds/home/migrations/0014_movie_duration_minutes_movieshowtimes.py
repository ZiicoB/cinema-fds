# Generated by Django 5.0.3 on 2024-06-24 17:59

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_movie_num_ratings_alter_rating_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='duration_minutes',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.CreateModel(
            name='MovieShowtimes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showtime1', models.TimeField(default=django.utils.timezone.now)),
                ('showtime2', models.TimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('showtime3', models.TimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('showtime4', models.TimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='showtimes', to='home.movie')),
            ],
        ),
    ]
