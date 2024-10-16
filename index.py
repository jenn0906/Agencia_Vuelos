from datetime import datetime

listaVuelos = []
viajes = []
idVuelos = 1 

while True :
    print("---\n Bienvenido a la agencia de vuelos islas tiqui tiqui----")
    print("1. A donde quieres ir?")
    print("2. Modificar mi vuelo")
    print("3. Eliminar mi vuelo")
    print("4. salir")

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
        print(listaVuelos[0])

    #en esta parte se deben mostrar los vuelos que puedo escoger
    print("---\n Escoge tu vuelo----")
    
    if pasajeros == "1" & destino == "medellin" :
        print(viajes)

   
    





        