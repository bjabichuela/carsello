# Generated by Django 4.0 on 2021-12-16 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_body_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='passengers',
            field=models.CharField(choices=[('2', '2'), ('4', '4'), ('6', '6'), ('8', '8'), ('10', '10'), ('12', '12')], max_length=10),
        ),
    ]
