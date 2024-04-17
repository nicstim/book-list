# Generated by Django 5.0.4 on 2024-04-17 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(max_length=255, verbose_name='Название столбца')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Флаг видимости столбца')),
            ],
            options={
                'verbose_name': 'Настройка столбцов',
                'verbose_name_plural': 'Настройки столбцов',
            },
        ),
    ]