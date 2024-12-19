import json

class Administrador:
    def __init__(self, CC, nombres, apellidos, direccion, telefonos, correo):
        self.CC = CC
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefonos = telefonos  
        self.correo = correo
     

    def to_dict(self):
        return {
            "CC": self.CC,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "direccion": self.direccion,
            "telefonos": self.telefonos,
            "correo": self.correo,        
        }
