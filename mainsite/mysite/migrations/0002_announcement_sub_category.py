# Generated by Django 4.0.4 on 2022-04-17 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='sub_category',
            field=models.ManyToManyField(to='mysite.subcategories'),
        ),
    ]