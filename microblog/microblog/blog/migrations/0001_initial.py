# Generated by Django 2.1.7 on 2019-02-21 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(max_length=140)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]