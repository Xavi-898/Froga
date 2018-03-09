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
        
class Alumno(Persona):
    def __init__(self,curso):
        self.curso = curso
        
class Asignatura:
    def __init__(self,nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
class Nota:
    def __init__(self, total, media):
        self.total = total
        self.media = media
