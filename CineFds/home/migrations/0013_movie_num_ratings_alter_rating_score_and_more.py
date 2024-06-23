# Generated by Django 5.0.3 on 2024-06-23 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_userrating_nota'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='num_ratings',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.FloatField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
        migrations.AlterField(
            model_name='userrating',
            name='nota',
            field=models.FloatField(),
        ),
    ]
