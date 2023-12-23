# Variables

my_str_variable="My String variable"
print(my_str_variable)

my_int_variable=5
print(my_int_variable)

my_int_to_str_variable=str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable=False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_str_variable, my_int_variable, my_bool_variable)
print(type(print("")))#cosa rara
print("Este es el valor de:",my_bool_variable)

# algunas funciones del sistema
print(len(my_str_variable)) #logitud de cadenas

# variables en una sola linea
name, surname, alias, edad = "Carlos","Rivas","cknox", 41
print("me llamo:",name,surname, "mi edad es:",edad,"y mi alias es:",alias)

# Inputs
'''
name=input('cuál es tu nombre? ')
age=input("cuántos años tienes? ")
print(name)
print(age)
'''

#cambiamos el tipo
name=35
age="Carlangas"
print(name)
print(age)

# forzamos el tipo?
address: str = "mi direccion"
address=32
print(type(address))
