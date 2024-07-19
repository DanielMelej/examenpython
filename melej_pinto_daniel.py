import random
import csv

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
trabajadores_sueldos = []

def asignar_sueldos_aleatorios():
    for trabajador in trabajadores:
        nombre = trabajador
        sueldo = random.randint(300000, 2500000)
        trabajadores_sueldos.append({"nombre": nombre, "sueldo" : sueldo})
    print(trabajadores_sueldos)

def clasificar_sueldos():
    menor = []
    medio = []
    mayor = []
    for i in trabajadores_sueldos:
        if int(i["sueldo"]) <= 800000:
            menor.append(i)
        elif int(i["sueldo"]) > 800000 and int(i["sueldo"]) < 2000000:
            medio.append(i)
        elif int(i["sueldo"]) >= 2000000:
            mayor.append(i)
    for i in menor:
        print(i)
    print(f"Los sueldo que son menores a $800.000 son: {len(menor)}")
    for i in medio:
        print(i)
    print(f"Los sueldo que se encuentra entre $800.000 a $2.000.0000 son: {len(medio)}")
    for i in mayor:
        print(i)
    print(f"Los sueldo que se encuentra entre $800.000 a $2.000.0000 son: {len(mayor)}")

def ver_estadisticas():
    for i in trabajadores_sueldos:
        minimo = min(todos_los_sueldos)
        maximo = max(todos_los_sueldos)
        promedio = sueldos / len(sueldos)

def Reporte_de_sueldos():
    with open("sueldos.csv", "w", newline = "") as documento:
        archivo = csv.writer(documento)
    pass
def salir_del_programa():
    print("Finalizando programa...\n"
          "Desarrollador por Daniel Melej\n"
          "RUT 19.689.217-6")

def menu():
    op = 0
    while op != 5:
        try:
            print("1. Asignar sueldos aleatorios\n"
                "2. Clasificar sueldos\n"
                "3. Ver estadísticas\n"
                "4. Reporte de sueldos\n"
                "5. Salir del programa\n")
            op = int(input("Ingrese la opcion que desea realzar: "))
            if op == 1:
                asignar_sueldos_aleatorios()
            elif op == 2:
                clasificar_sueldos()
            elif op == 3:
                Reporte_de_sueldos()
            elif op == 4:
                Reporte_de_sueldos()
            elif op == 5:
                salir_del_programa()
            else:
                print("Ingree una de las opciones validas")
        except ValueError as error_op:
            print("Opncio no valida")

menu()