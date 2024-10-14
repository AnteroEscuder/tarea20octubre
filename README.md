# Descipción

El proyecto representa el funcionamiento de una farmacia, simulando como sería este en la vida real, representando 10 modelos que se ven a continuación

<br>

# Esqueema base de datos Entidad Relación

![Imagen_base_datos](./assets/diagrama_entidad_relacion.png "Entidad Relación")

<br>

# Modelos

## Proveedor

Representa a los proveedores de medicamentos que surten la farmacia. Este modelo almacena la información de contacto de los proveedores, como su nombre, dirección, teléfono y correo electrónico.

```Python
nombre = models.CharField(max_length=100)
direccion = models.CharField(max_length=200)
telefono = models.CharField(max_length=15)
email = models.EmailField()
```

## Cliente

Almacena los datos de los clientes que realizan compras en la farmacia. Incluye el nombre, apellido, dirección, correo electrónico y número de teléfono de cada cliente.

```Python
nombre = models.CharField(max_length=100)
apellido = models.CharField(max_length=100)
direccion = models.CharField(max_length=200)
email = models.EmailField()
telefono = models.CharField(max_length=15)
```

## Medicamentos

Contiene los detalles de los medicamentos que vende la farmacia. Cada medicamento tiene un nombre, descripción, precio, cantidad en stock, fecha de caducidad, y está asociado a un proveedor específico.

```Python
nombre = models.CharField(max_length=100)
descripcion = models.TextField()
precio = models.DecimalField(max_digits=10, decimal_places=2)
stock = models.PositiveIntegerField()
fecha_caducidad = models.DateField()
proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
```

Representa las recetas médicas que los clientes presentan para comprar ciertos medicamentos. Cada receta está asociada a un cliente y contiene una descripción, el nombre de la compañía emisora, y las fechas de emisión y caducidad.

## Receta
```Python
cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
descripcion = models.TextField()
nombre_compania = models.CharField(max_length=100)
fecha_emision = models.DateField()
fecha_caducidad = models.DateField()
```

## Venta

Registra las ventas realizadas en la farmacia. Está vinculada a un cliente y los medicamentos comprados, así como la cantidad vendida, el precio total, la fecha de entrega y el correo electrónico de la farmacia.

```Python
cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
medicamentos = models.ManyToManyField(Medicamento)
fecha_entrega = models.DateField(auto_now_add=True)
cantidad = models.PositiveIntegerField()
precio = models.DecimalField(max_digits=10, decimal_places=2)
email_farmacia = models.EmailField()
```

## Empleado

Representa a los empleados que trabajan en la farmacia. Almacena el nombre, apellido, cargo y sueldo de cada empleado.

```Python
nombre = models.CharField(max_length=100)
apellido = models.CharField(max_length=100)
cargo = models.CharField(max_length=50)
sueldo = models.DecimalField(max_digits=10, decimal_places=2)
```

## Farmacia

Almacena los datos de la farmacia en sí, incluyendo su nombre, dirección, teléfono y correo electrónico. Cada farmacia tiene un propietario, que es un empleado, y puede tener varios empleados asociados.

```Python
nombre = models.CharField(max_length=100)
direccion = models.CharField(max_length=200)
telefono = models.CharField(max_length=15)
email = models.EmailField()
propietario = models.OneToOneField(Empleado, on_delete=models.CASCADE)
empleados = models.ManyToManyField(Empleado, related_name='farmacias')
```


## Pedido

Registra los pedidos de medicamentos que la farmacia hace a los proveedores. Cada pedido está vinculado a un proveedor, tiene un coste total, observaciones, y una fecha en la que se realizó el pedido.

```Python
proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
coste_total = models.DecimalField(max_digits=10, decimal_places=2)
observacion = models.TextField()
fecha_pedido = models.DateField()
```

## Inventario

Controla el stock disponible de los medicamentos. Cada entrada en el inventario está vinculada a un medicamento específico y almacena la cantidad disponible, la fecha de alta, baja y la última actualización del stock.

```Python
medicamento = models.OneToOneField(Medicamento, on_delete=models.CASCADE)
cantidad_disponible = models.PositiveIntegerField()
ultima_actualizacion = models.DateTimeField(auto_now=True)
fecha_alta = models.DateField(auto_now_add=True)
fecha_baja = models.DateField(blank=True, null=True)
```

## Categoria

Clasifica los medicamentos en diferentes categorías para su organización dentro de la farmacia. Cada categoría tiene un nombre, un nombre corto, observaciones y un color representativo, y puede estar relacionada con varios medicamentos.

```Python
nombre = models.CharField(max_length=50)
medicamentos = models.ManyToManyField(Medicamento, related_name='categorias')
nombre_corto = models.CharField(max_length=10)
observacion = models.TextField()
color = models.CharField(max_length=50)
```