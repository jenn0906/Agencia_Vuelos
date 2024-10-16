from datetime import datetime

listaVuelos = []

idVuelos = 1 

while True :
    print("---\n Bienvenido a la agencia de vuelos islas tiqui tiqui----")
    print("1. A donde quieres ir?")
    print("2. Leer todas las tarea")
    print("3. Actualizar una tarea")
    print("4. Eliminar una tarea")
    print("5. salir")

    opcion = input("Elige la opcion deseada: ")

    #Haciendo reservas-----------------------------------
    if opcion == "1":
        #en esta linea estamos pidiendo al usuario ingresar la informacion inicial para el vuelo
        origen = input("¿Cual es tu origen?")
        destino = input("Escriba su destino")
        pasajeros = input("Cantidad de pasajeros")
        fechaIda = input("Ingrese fecha de ida")
        fechaRegreso = input("Ingrese fecha de regreso")

        listaVuelos.append({"id": idVuelos, "origen": origen, "destino": destino, "pasajeros": pasajeros, "fecha de ida": fechaIda, "fecha de regreso": fechaRegreso})
        print(f"Tarea {idVuelos} creada con exito \n")
        idVuelos += 1

        fechaVencimiento = datetime.strptime(fechaVencimiento, "%d/%m/%y")

        #esto es una prueba
        #esto es una prueba

        