# Generated by Django 3.1.7 on 2021-07-03 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0003_ordermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(default='pending', max_length=10),
            preserve_default=False,
        ),
    ]