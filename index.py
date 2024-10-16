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
        
        #Lista de vuelos disponibles

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


    #-salir de la reserva-------

    # if opcion == "5":
    #      print("Muchas gracias por su visita")
    #      break

    # else:
    #      print("opcion invalida por favor verifique")       

#-----------------------------------PAQUETES TURISTICOS ------------------------------------

Paquete1 = {
    "nombre" : "TourMedellin",
    "duracion" : "cuatro dias y tres noches",
    "transporte" : "privado",
    "actividades" : "jardin botanico, parque explora, museo de arte moderno, comuna 13",
    "seguridad" : "seguro contra accidentes y asistencia medica",
    "precio": 360.000
}

Paquete2 = {
    "nombre" : "MedalloExtremo",
    "duracion" : "tres dias y dos noches",
    "transporte" : "privado",
    "actividades" : "parapente en guatape, visita a las cascadas de san luis, recorrido en cuatrimotos ",
    "seguridad" : " seguro contra accidentes y asistencia medica",
    "precio" : 650.000
}

#---------------------------------------------------------------------------------

Paquete3 = {
    "nombre" : "CartagenaBeach",
    "duracion" : "12 horas",
    "transporte" : "terrestre privado, lancha rapida",
    "actividades" : "excurción Bora bora beach, isabella y Pao Pao beach.",
    "alimentación": "coctel de binvenida, almuerzo, refrigerio, agua y gaseosa en la lancha",
    "seguridad" : "seguro contra accidentes y asistencia medica",
    "precio": 300.000
}






        