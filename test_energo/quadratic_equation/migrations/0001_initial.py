# Generated by Django 4.0.5 on 2022-06-07 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.IntegerField(blank=True, default=1)),
            ],
            options={
                'verbose_name': 'Equation',
                'verbose_name_plural': 'Equations',
            },
        ),
    ]