import os
from funciones import *

print('Bienvenido a Movistar')

def menu_principal():
        print( """""""""""
          Bienvenidos a Movistar 
          """"""""")
        print("1. Iniciar Sesion")
        print("2. Registrarse")
        print("3. Admin")
        print("4. Salir")


def main():
    while True:
        os.system('clear')
        menu_principal()
        opcion=int(input('Seleccione una opcion :'))


        if opcion == 1:
            usuario_data = {
                "CC": int(input("Numero de documento :")),
            }


            agregar_usuario(usuario_data)

        elif opcion ==2:
            usuario_data = {
                                 "CC": int(input("Numero de documento :")),
                "nombres": input("Nombres :"),
                "apellidos": input("Apellidos :"),
                "direccion": input("Dirección :"),
                "telefonos": int(input("Numero de telefono :")),
                "correo": input("Correo Electronico :"),
            }


            agregar_usuario(usuario_data)


        elif opcion ==3:
            administrador_data = {
                "Cedula": input("Digite su Cedula :"),
                "Clave": int(input("Digite la clave :")),
            }
            agregar_administrador(administrador_data)

                    
        else: opcion ==4
        os.system('clear')
        print('Hasta Pronto')
        break


if __name__ == "__main__":
    main()