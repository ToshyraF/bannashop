# Generated by Django 3.0.4 on 2020-03-15 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_name', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=264)),
                ('phonenmuber', models.CharField(blank=True, max_length=20, null=True)),
                ('level', models.CharField(max_length=1)),
                ('transpot', models.CharField(blank=True, max_length=264, null=True)),
                ('province_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setting.Province')),
                ('region_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setting.Region')),
            ],
        ),
        migrations.AddField(
            model_name='province',
            name='region_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setting.Region'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=264)),
                ('cost', models.IntegerField()),
                ('number', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setting.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setting.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='province_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setting.Province'),
        ),
        migrations.AddField(
            model_name='order',
            name='region_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setting.Region'),
        ),
        migrations.AddField(
            model_name='order',
            name='shop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setting.Shop'),
        ),
    ]
