import json
from usuario import Usuario
from administrador import Administrador

def cargar_json(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def guardar_json(ruta_archivo, datos):
    with open(ruta_archivo, 'w') as f:
        json.dump(datos, f, indent=2)


def agregar_usuario(Usuario_data, ruta_archivo="Usuario.json"):

    usuario = cargar_json(ruta_archivo)
    nuevo_usuario = usuario(**Usuario_data)
    usuario.append(nuevo_usuario.to_dict())
    guardar_json(ruta_archivo, usuario)
    print(f"Usuario {nuevo_usuario.nombres} {nuevo_usuario.apellidos} agregado correctamente.")



def agregar_administrador(Administrador_data, ruta_archivo="Administrador.json"):
    Administrador = cargar_json(ruta_archivo)
    Administrador = Administrador(Administrador_data)
    Administrador.append(Administrador.to_dict())
    guardar_json(ruta_archivo, Administrador)
    print(f"Administrador {Administrador.nombres} {Administrador.apellidos} agregado correctamente.")


