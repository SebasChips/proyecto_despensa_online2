# Generated by Django 4.2.6 on 2023-11-06 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoría',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripción', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('imagen_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contraseña', models.CharField(max_length=255)),
                ('dirección', models.CharField(max_length=255)),
                ('teléfono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(max_length=50)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.usuario')),
            ],
        ),
    ]