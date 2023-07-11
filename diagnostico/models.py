from django.db import models

# Create your models here.
class Diagnostico(models.Model):
    nombrepaciente = models.CharField(max_length=100)
    nivelazucar = models.DecimalField(max_digits=5,decimal_places=2)
    nivelgrasa = models.DecimalField(max_digits=5,decimal_places=2)
    niveloxigeno = models.DecimalField(max_digits=5,decimal_places=2)
    riesgo = models.CharField(max_length=5,blank=True, null=True)

    @classmethod
    def calculate_risk_level(cls, nivelazucar, nivelgrasa, niveloxigeno):
        if nivelazucar > 70 and nivelgrasa > 88.5 and niveloxigeno < 60:
            return "Alto"
        if 50 <= nivelazucar <= 70 and 62.2 <= nivelgrasa <= 88.5 and  60 <= niveloxigeno <= 70:
            return "Medio"
        if (nivelazucar < 50 and nivelgrasa < 62.2 and niveloxigeno > 70):
            return "Bajo"
        
    def save(self, *args, **kwargs):
        self.riesgo = self.calculate_risk_level(self.nivelazucar, self.nivelgrasa, self.niveloxigeno)
        super().save(*args, **kwargs)
    


    def __str__(self) -> str:
        return f"{self.nombrepaciente}"
