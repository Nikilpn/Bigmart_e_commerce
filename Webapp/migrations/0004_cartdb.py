# Generated by Django 5.0.4 on 2024-06-01 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0003_registerdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USERNAME', models.CharField(blank=True, max_length=100, null=True)),
                ('PRODUCTNAME', models.CharField(blank=True, max_length=100, null=True)),
                ('QUANTITY', models.IntegerField(blank=True, null=True)),
                ('TOTALPRICE', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]