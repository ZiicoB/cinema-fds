# Generated by Django 5.0.3 on 2024-06-24 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_movie_showtime1_movie_showtime2_movie_showtime3_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='showtime1',
            new_name='horario1',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='showtime2',
            new_name='horario2',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='showtime3',
            new_name='horario3',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='showtime4',
            new_name='horario4',
        ),
    ]
