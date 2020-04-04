# Generated by Django 2.2.11 on 2020-04-03 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_pic_classify'),
    ]

    operations = [
        migrations.AddField(
            model_name='pic',
            name='is_on_home_page',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pic',
            name='image',
            field=models.ImageField(default=None, upload_to='gallery'),
        ),
    ]