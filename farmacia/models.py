from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del proveedor", help_text="Nombre completo del proveedor")
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    frecuente = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100, db_column="medicamento_nombre")
    descripcion = models.TextField(db_comment="Descripción del medicamento", default="No hay descripción disponible")
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)], db_index=True)
    stock = models.PositiveIntegerField()
    fecha_caducidad = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return self.nombre
    
class Receta(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    nombre_compania = models.CharField(max_length=100)
    fecha_emision = models.DateField()
    fecha_caducidad = models.DateField()

class Venta (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    medicamentos = models.ManyToManyField(Medicamento)
    fecha_entrega = models.DateField(auto_now_add=True)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    email_farmacia = models.EmailField(),
    recibo = models.CharField(max_length=100, unique_for_date="fecha_venta", unique_for_month="fecha_venta", unique_for_year="fecha_venta")

class Empleado (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Farmacia (models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    url_web = models.URLField()
    propietario = models.OneToOneField(Empleado, on_delete=models.CASCADE)
    empleados = models.ManyToManyField(Empleado, related_name='farmacias')

    def __str__(self):
        return self.nombre
    
class Pedido (models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    coste_total = models.DecimalField(max_digits=10, decimal_places=2)
    observacion = models.TextField()
    fecha_pedido = models.DateField()
    # medicamentos = models.ManyToManyField(Medicamento, through='PedidoMedicamento', related_name='pedidos_medicamentos')

class Inventario (models.Model):
    medicamento = models.OneToOneField(Medicamento, on_delete=models.CASCADE)
    cantidad_disponible = models.PositiveIntegerField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField(blank=True, null=True)
    farmacia = models.OneToOneField(Farmacia, on_delete=models.CASCADE)

# class PedidoMedicamento(models.Model):
#     pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='pedido_medicamentos')
#     medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, related_name='pedido_medicamentos')
#     cantidad = models.PositiveIntegerField()
#     precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
#     fecha_vencimiento = models.DateField()
#     observacion = models.TextField()

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    medicamentos = models.ManyToManyField(Medicamento, related_name='categorias')
    nombre_corto = models.CharField(max_length=10)
    observacion = models.TextField()
    color = models.CharField(max_length=50)