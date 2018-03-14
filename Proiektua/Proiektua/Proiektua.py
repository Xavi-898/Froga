'''
Created on 7 mar. 2018

@author: DM3-1-07
'''


class Persona(object):
   


    def __init__(self, dni, nombre, apellidos, direccion, telefono, email):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        print('')
 
class Profesor(Persona):
    def __init__(self,departamento):
        self.departamento = departamento
    def bistaratu(self):
        print(self.__dict__)     
class Alumno(Persona):
    def __init__(self,curso):
        self.curso = curso
        
class Asignatura:
    def __init__(self,nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
    def bistaratu(self):
        print(self.__dict__)

class Nota:
    def __init__(self, total, media):
        self.total = total
        self.media = media
    def bistaratu(self):
        print(self.__dict__)

A1 = Asignatura('a','b')
A1.bistaratu()
N1=Nota(8,7)
N1.bistaratu()