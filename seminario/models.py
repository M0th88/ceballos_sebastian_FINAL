from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class Inscrito(models.Model):
    ESTADO_CHOICES = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO ASISTEN', 'No Asisten'),
    ]

    nombre = models.CharField(max_length=80)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)  # Relación ForeignKey
    nro_personas = models.PositiveIntegerField()
    telefono = models.CharField(max_length=15)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    hora_inscripcion = models.TimeField(auto_now_add=True)
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES)
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.institucion}"
