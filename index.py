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
        fecha_Ida = input("Ingrese fecha de ida (dd/mm/aaaa): ")
        fecha_Regreso = input("Ingrese fecha de regreso (dd/mm/aaaa):")

        listaVuelos.append({"id": idVuelos, "origen": origen, "destino": destino, "pasajeros": pasajeros, "fecha de ida": fecha_Ida, "fecha de regreso": fecha_Regreso})
        print(f"Tarea {idVuelos} creada con exito \n")
        idVuelos += 1
#editar_vuelo------------------------------------------------------------------------------------------------------------------------
    if opcion == "2":
      vuelo_encontrado = False
    idActualizar = int(input("Ingrese el ID del vuelo que quiere actualizar: "))
    
    for i in viajes:
        if i["id"] == idActualizar:
            nuevoOrigen = input("Ingrese el nuevo origen (dejar en blanco si no quiere modificarlo): ")
            nuevoDestino = input("Ingrese el nuevo destino (dejar en blanco si no quiere modificarlo): ")
            nuevosPasajeros = input("Ingrese la nueva cantidad de pasajeros (dejar en blanco si no quiere modificarla): ")
            nuevaFechaIda = input("Ingrese una nueva fecha (dejar en blanco si no quiere modificarla): ")
            nuevaFechaRegreso = input("Ingrese una nueva fecha (dejar en blanco si no quiere modificarla): ")
            
            if nuevoOrigen:
                i["origen"] = nuevoOrigen
            if nuevoDestino:
                i["destino"] = nuevoDestino
            if nuevosPasajeros:
                i["pasajeros"] = nuevosPasajeros
            if nuevaFechaIda:
                i["fecha_ida"] = nuevaFechaIda
            if nuevaFechaRegreso:
                i["fecha_regreso"] = nuevaFechaRegreso

                
            print(f"Vuelo {idActualizar} actualizado con éxito.\n")
            vuelo_encontrado = True
            break
    
    if not vuelo_encontrado:
        print(f"No se encontró el vuelo con el ID: {idActualizar}\n")


    #Eliminar reserva-------------------------------------     
    elif opcion == "4":
        idEliminar = int(input("Ingrese el ID a eliminar: "))
        vuelo_encontrado = False
        for i in idVuelos :
            if i ["id"] == idEliminar:  
                idVuelos.remove(i) 
                print(f"Tarea {idEliminar} eliminada exitosamente ")
                vuelo_encontrado = True
                break
        if not vuelo_encontrado :
            print(f" No se encontro el vuelo con el ID {idEliminar}")     

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


listaPaquetesTuristicos = [
    {
        "nombre": "TourMedellín",
        "duracion": "3 dias",
        "transporte": "privado",
        "actividades": "jardin botanico, parque explora, museo de arte moderno, comuna 13",
        "seguridad" : "seguro contra accidentes y asistencia medica"
    },
       {
        "nombre" : "MedalloExtremo",
        "duracion" : "tres dias y dos noches",
        "transporte" : "privado",
        "actividades" : "parapente en guatape, visita a las cascadas de san luis, recorrido en cuatrimotos ",
        "seguridad" : "seguro contra aciddente y asistencia medica" 
    }, 
       {
        "nombre" : "CartagenaBeach",
        "duracion" : "12 horas",
        "transporte" : "terrestre privado, lancha rapida",
        "actividades" : "excurción Bora bora beach, isabella y Pao Pao beach.",
        "alimentacion": "coctel de binvenida, almuerzo, refrigerio, agua y gaseosa en la lancha",
        "seguridad" : "seguro contra accidentes y asistencia medica", 
       }

]

idpaquetes = 1

while True :
    print("---\n Bienvenido a nuestra seccion de paquetes Turisticos---")
    print("1. TourMedellin ")
    print("2. MedalloExtremo")
    print("3. CartagenaBeach")
    print("4. salir")
    
    opcion = input("por favor, elige el paquete turistico que mas te llame la atencion  ")

    if opcion == "1":
        paquete = listaPaquetesTuristicos[0]
        print(f"\n detalles del {paquete['nombre']}")
        print(f"Duracion: {paquete['duracion']}")
        print(f"Transporte: {paquete['transporte']}")
        print(f"Actividades: {paquete['actividades']}")
        print(f"Seguridad: {paquete['seguridad']}")

    elif opcion == "2": 
        paquete = listaPaquetesTuristicos[1]
        print(f"\ndetalles del {paquete['nombre']}")
        print(f"Duracion: {paquete['duracion']}")
        print(f"Transporte: {paquete['transporte']}")
        print(f"Actividades: {paquete['actividades']}")
        print(f"Seguridad: {paquete['seguridad']}")

    elif opcion == "3":
        paquete = listaPaquetesTuristicos[2]
        print(f"\ndetalles del {paquete['nombre']}")
        print(f"Duracion: {paquete['duracion']}")
        print(f"Transporte: {paquete['transporte']}")
        print(f"Actividades: {paquete['actividades']}")
        print(f"Seguridad: {paquete['seguridad']}")


    elif opcion == "4":
        print("\nGracias por visitar nuestra seccion de paquetes turisticos")
        break
    else : 
        print("opcion invalidad, porfavor elige una opcion de el 1 al 4")






        