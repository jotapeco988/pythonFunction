#punto 3 -Crear una subrutina llamada “Login”, que recibe un nombre de usuario y 
#una contraseña y te devuelve Verdadero si el nombre de usuario es “admin” y la 
#contraseña es “admin123*”. Además recibe el número de intentos que se ha intentado
# hacer login y si no se ha podido hacer login incremente este valor.

usuario = input("Introduzca su nombre de usuario: ")
contraseña = input("Introduzca su contraseña: ")
def login(usuario, contraseña):

    if usuario == "admin" and contraseña == "admin123":
        
        return True, 
    else:
        return False, 


resultado=login(usuario,contraseña)
print(resultado)
