from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class UserRol(models.Model):

    key = models.IntegerField(
    	verbose_name = u'Llave'
    	) 

    name = models.CharField(
    	verbose_name=u'Nombre',
    	max_length = 200
    	)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Rol de usuario'
        verbose_name_plural = u'Roles de usuarios'   

class ConnectionType(models.Model):

    key = models.IntegerField(
        verbose_name = u'Llave'
        ) 

    name = models.CharField(
        verbose_name=u'Nombre',
        max_length = 200
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Tipo de conexión'
        verbose_name_plural = u'Tipos de conexiones'   


class Sentences(models.Model):


    name = models.CharField(
        verbose_name=u'Nombre',
        max_length = 200
        )

    dbtype = models.ForeignKey(
        'ConnectionType',on_delete=models.CASCADE,
        verbose_name=u'Tipo de base de datos'
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Sentencia'
        verbose_name_plural = u'Sentencias'  



class SystemUser(models.Model):

    user = models.OneToOneField(
        'auth.User',
        verbose_name = u'Usuario',
    ) 

    rol = models.ForeignKey(
    	'UserRol',on_delete=models.CASCADE,
    	verbose_name=u'Rol del usuario'
    	)

    identification  = models.CharField(
        max_length=100,
        verbose_name=u'Número de identificacion',
        null = True,
    )


    cellphone = models.CharField(
        max_length=80,
        verbose_name=u'Número de celular',
        null = True,
    )
       

    def __str__(self):
        return self.user.get_username()

    class Meta:
        verbose_name = u'Usuario'
        verbose_name_plural = u'Usuarios'   





class ConectionData(models.Model):

    username = models.CharField(
        max_length=300,
        verbose_name=u'Nombre de usuario',
    )


    password = models.CharField(
        max_length=300,
        verbose_name=u'Contaseña',
    )

    dbname = models.CharField(
        max_length=300,
        verbose_name=u'Nombre de la base de datos',
    )

    host = models.CharField(
        max_length=300,
        verbose_name=u'Host',
    )

    dbtype = models.ForeignKey(
        'ConnectionType',on_delete=models.CASCADE,
        verbose_name=u'Tipo de base de datos'
        )

    port = models.CharField(
        max_length=100,
        verbose_name=u'Puerto',
        null=True,
        blank=True,
        )


    def __str__(self):
        return self.dbname

    class Meta:
        verbose_name = u'Datos de conexión'
        verbose_name_plural = u'Datos de conexiones'   
        
