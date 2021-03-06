# Generated by Django 3.1.2 on 2020-10-16 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Title')),
                ('description', models.TextField(max_length=50, verbose_name='Description')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created at')),
            ],
        ),
    ]
