# Generated by Django 3.0.3 on 2020-02-11 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BoatifyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=196)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]
