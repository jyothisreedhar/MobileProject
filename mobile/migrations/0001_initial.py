# Generated by Django 3.1.7 on 2021-05-06 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=120)),
                ('price', models.FloatField()),
                ('specs', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
