# Generated by Django 4.1.4 on 2023-07-04 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bar_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bar_code', models.ImageField(blank=True, upload_to='all_image_code/barcodes_images/')),
            ],
        ),
    ]
