# Generated by Django 4.2.2 on 2023-06-25 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oderitem',
            old_name='qunatity',
            new_name='quantity',
        ),
    ]
