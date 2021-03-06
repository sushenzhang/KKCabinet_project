# Generated by Django 2.2.11 on 2020-04-02 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_pic_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classify', models.CharField(default='N/A', max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='color',
            name='black',
        ),
        migrations.RemoveField(
            model_name='color',
            name='brown',
        ),
        migrations.RemoveField(
            model_name='color',
            name='grey',
        ),
        migrations.RemoveField(
            model_name='color',
            name='white',
        ),
        migrations.RemoveField(
            model_name='material',
            name='stone',
        ),
        migrations.RemoveField(
            model_name='material',
            name='wood',
        ),
        migrations.RemoveField(
            model_name='pic',
            name='object',
        ),
        migrations.AddField(
            model_name='color',
            name='color',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='material',
            name='material',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.RemoveField(
            model_name='pic',
            name='color',
        ),
        migrations.AddField(
            model_name='pic',
            name='color',
            field=models.ManyToManyField(to='app.Color'),
        ),
        migrations.AlterField(
            model_name='pic',
            name='image',
            field=models.ImageField(default='./app/static/app/images/1318967_1.jpg', upload_to='./app/static/app/images/gallery'),
        ),
        migrations.RemoveField(
            model_name='pic',
            name='material',
        ),
        migrations.AddField(
            model_name='pic',
            name='material',
            field=models.ManyToManyField(to='app.Material'),
        ),
        migrations.DeleteModel(
            name='Object',
        ),
    ]
