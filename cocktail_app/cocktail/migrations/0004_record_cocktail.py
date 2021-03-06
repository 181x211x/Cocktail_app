# Generated by Django 2.1.2 on 2019-02-20 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0003_auto_20190219_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record_Cocktail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('base', models.CharField(max_length=128)),
                ('lengh', models.CharField(max_length=128)),
                ('tech', models.CharField(max_length=128)),
                ('alc', models.IntegerField(null=True)),
                ('taste', models.CharField(max_length=128)),
                ('material1', models.CharField(max_length=128, null=True)),
                ('material2', models.CharField(max_length=128, null=True)),
                ('contents', models.CharField(max_length=128, null=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
