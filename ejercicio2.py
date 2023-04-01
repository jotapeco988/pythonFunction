#-Crea una función  que reciba una lista con valores
# numéricos y devuelva el valor máximo y el mínimo ingresados
def contador(lista):
    minimo = min(lista)
    maximo = max(lista)
    return minimo, maximo

lista = [10, 3, 0, 14, 22]
minimo, maximo = contador(lista)

print("El valor minimo es:", minimo)
print("El valor máximo es:", maximo)
