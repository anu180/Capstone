# Generated by Django 3.1.5 on 2021-05-01 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curd', '0003_auto_20210501_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='emp_pic',
            field=models.ImageField(default=0, upload_to='images/'),
            preserve_default=False,
        ),
    ]
