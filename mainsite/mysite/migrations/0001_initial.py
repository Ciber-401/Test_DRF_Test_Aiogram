# Generated by Django 4.0.4 on 2022-04-17 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название подкатегории')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.category')),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=100, verbose_name='Заглавление')),
                ('descriptions', models.TextField(verbose_name='Описание обьявления')),
                ('image', models.ImageField(upload_to='media/Y%/m%/%d', verbose_name='Изображение')),
                ('data_published', models.DateTimeField()),
                ('category', models.ManyToManyField(to='mysite.category')),
            ],
        ),
    ]
