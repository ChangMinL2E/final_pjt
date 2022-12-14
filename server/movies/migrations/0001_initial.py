# Generated by Django 3.2.13 on 2022-11-17 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('release_date', models.DateField(null=True)),
                ('vote_average', models.FloatField(default=0, null=True)),
                ('img_url', models.CharField(max_length=255, null=True)),
                ('backdrop_img_url', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('movies', models.ManyToManyField(related_name='genres', to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('gender', models.IntegerField()),
                ('job', models.CharField(max_length=255)),
                ('popularity', models.FloatField()),
                ('profile_img_path', models.CharField(max_length=255)),
                ('movies', models.ManyToManyField(related_name='crews', to='movies.Movie')),
            ],
        ),
    ]
