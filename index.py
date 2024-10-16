from datetime import datetime

listaVuelos = []
viajes = [
    {
        "ciudad": "Medellín",
        "precio": "$40",
        "duración": "cuatro días y 3 noches",
        "caminata": "es un paseo en el cerro"
    },
       {
        "ciudad": "Cartagena",
        "precio": "$400",
        "duración": "2 días y 1 noche",
        "caminata": "es un paseo"
    },

]

idVuelos = 1 

while True :
    print("---\n Bienvenido a la agencia de vuelos islas tiqui tiqui----")
    print("1. A donde quieres ir?")
    print("2. Modificar mi vuelo")
    print("3. Eliminar mi vuelo")
    print("4. Mostrar mis reservas")
    print("5. salir")

    opcion = input("Elige la opcion deseada: ")

    #Haciendo reservas-----------------------------------
    if opcion == "1":
        #en esta linea estamos pidiendo al usuario ingresar la informacion inicial para el vuelo
        origen = input("¿Cual es tu origen?: ")
        destino = input("Escriba su destino: ")
        pasajeros = input("Cantidad de pasajeros en numeros: ")
        fechaIda = input("Ingrese fecha de ida (dd/mm/aaaa): ")
        fechaRegreso = input("Ingrese fecha de regreso (dd/mm/aaaa):")

        listaVuelos.append({"id": idVuelos, "origen": origen, "destino": destino, "pasajeros": pasajeros, "fecha de ida": fechaIda, "fecha de regreso": fechaRegreso})
        print(f"Tarea {idVuelos} creada con exito \n")
        idVuelos += 1

        #fechaVencimiento = datetime.strptime(fechaVencimiento, "%d/%m/%y")
        print(listaVuelos[:])

    #en esta parte se deben mostrar los vuelos que puedo escoger
    print("---\n Escoge tu vuelo----")
    
    if  listaVuelos[0]["destino"].lower() == "medellin" :
        print(viajes[0])
    
    elif listaVuelos[0]["destino"].lower() == "cartagena" :
        print(viajes[1])

    if opcion == "4":
        if len(listaVuelos)== 0:
            print("No hay listaVuelos..")
        else:
            print("-LISTA DE TAREAS-")
        for i in listaVuelos:
            print(f"ID: {i["id"]} Origen: {i["origen"]} Destino: {i["destino"]}")
            print()


    elif opcion == "5":
        print("Muchas gracias Feliz día")
        break
    else:
        print("opcion invalida por favor verifique")
    





        