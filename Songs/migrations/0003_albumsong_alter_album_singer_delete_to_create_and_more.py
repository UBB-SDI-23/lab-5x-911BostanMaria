# Generated by Django 4.1.7 on 2023-03-27 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Songs', '0002_album_singer_to_create_album_singer'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copies_sold', models.BigIntegerField()),
                ('grammys', models.BigIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='Songs.singer'),
        ),
        migrations.DeleteModel(
            name='To_Create',
        ),
        migrations.AddField(
            model_name='albumsong',
            name='album_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Songs.album'),
        ),
        migrations.AddField(
            model_name='albumsong',
            name='song_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Songs.song'),
        ),
    ]