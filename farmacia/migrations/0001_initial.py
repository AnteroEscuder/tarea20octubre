# Generated by Django 5.1.2 on 2024-10-14 22:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=50)),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('fecha_caducidad', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Farmacia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('empleados', models.ManyToManyField(related_name='farmacias', to='farmacia.empleado')),
                ('propietario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='farmacia.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_disponible', models.PositiveIntegerField()),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('fecha_alta', models.DateField(auto_now_add=True)),
                ('fecha_baja', models.DateField(blank=True, null=True)),
                ('farmacia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='farmacia.farmacia')),
                ('medicamento', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='farmacia.medicamento')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nombre_corto', models.CharField(max_length=10)),
                ('observacion', models.TextField()),
                ('color', models.CharField(max_length=50)),
                ('medicamentos', models.ManyToManyField(related_name='categorias', to='farmacia.medicamento')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coste_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('observacion', models.TextField()),
                ('fecha_pedido', models.DateField()),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmacia.proveedor')),
            ],
        ),
        migrations.AddField(
            model_name='medicamento',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmacia.proveedor'),
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('nombre_compania', models.CharField(max_length=100)),
                ('fecha_emision', models.DateField()),
                ('fecha_caducidad', models.DateField()),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='farmacia.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrega', models.DateField(auto_now_add=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('email_farmacia', models.EmailField(max_length=254)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmacia.cliente')),
                ('medicamentos', models.ManyToManyField(to='farmacia.medicamento')),
            ],
        ),
    ]
