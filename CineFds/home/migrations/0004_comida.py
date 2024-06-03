# Generated by Django 5.0.3 on 2024-06-02 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('imagem', models.ImageField(upload_to='comidas/')),
            ],
        ),
    ]