# Generated by Django 3.1.4 on 2020-12-03 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20201203_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('price', models.FloatField()),
                ('amount', models.BigIntegerField()),
                ('min_amount', models.IntegerField()),
                ('detail', models.TextField()),
                ('status', models.CharField(choices=[('True', 'Yes'), ('False', 'No')], max_length=10, null=True)),
                ('slug', models.SlugField(max_length=140, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
    ]