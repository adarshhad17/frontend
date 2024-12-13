# Generated by Django 5.1.4 on 2024-12-13 15:34

import django.db.models.deletion
import uuid
import versatileimagefield.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubVariants',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('stock', models.DecimalField(decimal_places=8, default=0.0, max_digits=20)),
            ],
            options={
                'verbose_name': 'sub_variant',
                'verbose_name_plural': 'sub_variants',
                'db_table': 'products_sub_variants',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ProductID', models.BigIntegerField(unique=True)),
                ('ProductCode', models.CharField(max_length=255, unique=True)),
                ('ProductName', models.CharField(max_length=255)),
                ('ProductImage', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='uploads/')),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedDate', models.DateTimeField(blank=True, null=True)),
                ('IsFavourite', models.BooleanField(default=False)),
                ('Active', models.BooleanField(default=True)),
                ('HSNCode', models.CharField(blank=True, max_length=255, null=True)),
                ('TotalStock', models.DecimalField(blank=True, decimal_places=8, default=0.0, max_digits=20, null=True)),
                ('CreatedUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user%(class)s_objects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'products_product',
                'ordering': ('-CreatedDate', 'ProductID'),
                'unique_together': {('ProductCode', 'ProductID')},
            },
        ),
        migrations.CreateModel(
            name='StockManagement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('change', models.DecimalField(decimal_places=8, max_digits=20)),
                ('reason', models.CharField(choices=[('PURCHASE', 'Purchase'), ('SALE', 'Sale')], max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sub_variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_records', to='products.subvariants')),
            ],
            options={
                'verbose_name': 'stock_management',
                'verbose_name_plural': 'stock_management',
                'db_table': 'products_stock_management',
            },
        ),
        migrations.CreateModel(
            name='Variants',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='products.products')),
            ],
            options={
                'verbose_name': 'variant',
                'verbose_name_plural': 'variants',
                'db_table': 'products_variants',
            },
        ),
        migrations.AddField(
            model_name='subvariants',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_variants', to='products.variants'),
        ),
    ]
