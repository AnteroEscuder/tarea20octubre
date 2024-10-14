# Esqueema base de datos Entidad Relación

![Imagen_base_datos](./assets/diagrama_entidad_relacion.png "Entidad Relación")

# Modelos

## Proveedor

```Python
nombre = models.CharField(max_length=100)
direccion = models.CharField(max_length=200)
telefono = models.CharField(max_length=15)
email = models.EmailField()
```

## Cliente


```Python
nombre = models.CharField(max_length=100)
apellido = models.CharField(max_length=100)
direccion = models.CharField(max_length=200)
email = models.EmailField()
telefono = models.CharField(max_length=15)
```

## Medicamentos

```Python
nombre = models.CharField(max_length=100)
descripcion = models.TextField()
precio = models.DecimalField(max_digits=10, decimal_places=2)
stock = models.PositiveIntegerField()
fecha_caducidad = models.DateField()
proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
```

## Receta
```Python
cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
descripcion = models.TextField()
nombre_compania = models.CharField(max_length=100)
fecha_emision = models.DateField()
fecha_caducidad = models.DateField()
```

## Venta
```Python
cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
medicamentos = models.ManyToManyField(Medicamento)
fecha_entrega = models.DateField(auto_now_add=True)
cantidad = models.PositiveIntegerField()
precio = models.DecimalField(max_digits=10, decimal_places=2)
email_farmacia = models.EmailField()
```

## Empleado
```Python
nombre = models.CharField(max_length=100)
apellido = models.CharField(max_length=100)
cargo = models.CharField(max_length=50)
sueldo = models.DecimalField(max_digits=10, decimal_places=2)
```


## Farmacia
```Python
nombre = models.CharField(max_length=100)
direccion = models.CharField(max_length=200)
telefono = models.CharField(max_length=15)
email = models.EmailField()
propietario = models.OneToOneField(Empleado, on_delete=models.CASCADE)
empleados = models.ManyToManyField(Empleado, related_name='farmacias')
```


## Pedido
```Python
proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
coste_total = models.DecimalField(max_digits=10, decimal_places=2)
observacion = models.TextField()
fecha_pedido = models.DateField()
```

## Inventario
```Python
medicamento = models.OneToOneField(Medicamento, on_delete=models.CASCADE)
cantidad_disponible = models.PositiveIntegerField()
ultima_actualizacion = models.DateTimeField(auto_now=True)
fecha_alta = models.DateField(auto_now_add=True)
fecha_baja = models.DateField(blank=True, null=True)
```

## Categoria
```Python
nombre = models.CharField(max_length=50)
medicamentos = models.ManyToManyField(Medicamento, related_name='categorias')
nombre_corto = models.CharField(max_length=10)
observacion = models.TextField()
color = models.CharField(max_length=50)
```

# Esquema entidad relación

