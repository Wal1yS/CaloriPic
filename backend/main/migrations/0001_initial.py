# Generated by Django 5.2.4 on 2025-07-31 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Name')),
                ('content', models.TextField(verbose_name='Content')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
        ),
    ]
