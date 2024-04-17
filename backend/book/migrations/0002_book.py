# Generated by Django 5.0.4 on 2024-04-17 09:09

from django.db import migrations, models


def create_profile(apps, schema_editor):
    Profile = apps.get_model('book', 'Profile')
    Profile.objects.bulk_create([
        Profile(
            column_name=field,
            is_visible=True
        )
        for field in ["title", "name", "author", "price", "description"]

    ])


class Migration(migrations.Migration):
    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                (
                    'id',
                    models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('title', models.CharField(blank=True, max_length=30, null=True, verbose_name='Заголовок')),
                ('author', models.CharField(max_length=30, verbose_name='Автор')),
                ('description', models.CharField(blank=True, max_length=512, null=True, verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.RunPython(create_profile),
    ]
