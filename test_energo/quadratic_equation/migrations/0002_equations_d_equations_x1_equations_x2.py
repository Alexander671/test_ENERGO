# Generated by Django 4.0.5 on 2022-06-07 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quadratic_equation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equations',
            name='d',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='equations',
            name='x1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='equations',
            name='x2',
            field=models.FloatField(null=True),
        ),
    ]