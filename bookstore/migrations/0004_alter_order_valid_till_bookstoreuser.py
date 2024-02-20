# Generated by Django 5.0.2 on 2024-02-20 06:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('bookstore', '0003_alter_order_valid_till_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='valid_till',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 27, 12, 7, 26, 640869)),
        ),
        migrations.CreateModel(
            name='BookStoreUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=128)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, to='auth.group')),
            ],
        ),
    ]