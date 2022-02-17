# Generated by Django 4.0.2 on 2022-02-17 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350)),
                ('author', models.CharField(max_length=50)),
                ('points', models.IntegerField()),
                ('comments', models.IntegerField()),
                ('link', models.URLField()),
            ],
        ),
    ]