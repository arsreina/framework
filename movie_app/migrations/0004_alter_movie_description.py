# Generated by Django 4.1.2 on 2022-11-02 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_alter_review_movie_alter_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(null=True),
        ),
    ]