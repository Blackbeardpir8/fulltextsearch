# Generated by Django 5.0.7 on 2024-08-02 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('brand', models.CharField()),
                ('sku', models.CharField()),
                ('thumbnail', models.URLField(max_length=1000)),
            ],
        ),
    ]
