# Generated by Django 3.1.1 on 2020-10-08 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20201007_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]