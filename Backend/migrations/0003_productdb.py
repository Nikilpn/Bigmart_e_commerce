# Generated by Django 5.0.4 on 2024-05-09 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_rename_vegetabledb_categorydb'),
    ]

    operations = [
        migrations.CreateModel(
            name='productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATEGORY', models.CharField(blank=True, max_length=100, null=True)),
                ('PRODUCTNAME', models.CharField(blank=True, max_length=100, null=True)),
                ('PRODUCTPRICE', models.IntegerField(blank=True, null=True)),
                ('PRODUCTDESCRIPTION', models.CharField(blank=True, max_length=100, null=True)),
                ('PRODUCTIMAGE', models.ImageField(blank=True, null=True, upload_to='productimages')),
            ],
        ),
    ]
