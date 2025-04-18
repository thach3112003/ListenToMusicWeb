# Generated by Django 5.1.7 on 2025-03-30 18:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('album_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('deception', models.TextField(blank=True, null=True)),
                ('total_tracks', models.IntegerField(blank=True, null=True)),
                ('releasedate', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'albums',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('artist_id', models.AutoField(primary_key=True, serialize=False)),
                ('popularity_score', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('gener', models.CharField(blank=True, max_length=255, null=True)),
                ('follower', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'artists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlaylistOder',
            fields=[
                ('playlist_oder_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('datte_oder', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'playlist_oder',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Playlists',
            fields=[
                ('playlist_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('ispublic', models.IntegerField(blank=True, null=True)),
                ('track', models.IntegerField(blank=True, null=True)),
                ('releasedate', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'playlists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=255)),
                ('deception', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'roles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('track_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('is_copyright', models.IntegerField(blank=True, db_column='is_Copyright', null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('image_url', models.TextField(blank=True, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tracks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=255, unique=True)),
                ('passwordhash', models.CharField(max_length=255)),
                ('fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('accesstoken', models.TextField(blank=True, null=True)),
                ('refreshtoken', models.TextField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('image_user', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlaylistsDetail',
            fields=[
                ('playlist', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='music.playlists')),
            ],
            options={
                'db_table': 'playlists_detail',
                'managed': False,
            },
        ),
    ]
