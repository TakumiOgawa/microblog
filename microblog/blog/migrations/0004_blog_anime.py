# Generated by Django 2.1.7 on 2019-02-28 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190224_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='anime',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
