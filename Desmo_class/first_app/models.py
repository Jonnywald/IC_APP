from django.db import models

class Resposta(models.Model):
    Num_Pergunta = models.IntegerField(unique=True)
    Resposta = models.IntegerField()

    def __str__(self):
        return str(self.Num_Pergunta)
        
class Users(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=264,unique=True)

    def __str__(self):
        return str(self.email)
# Create your models here.
