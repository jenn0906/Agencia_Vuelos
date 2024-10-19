
listaVuelos = []
viajes = [
    {
        "ciudad": "Medellín",
        "precio": "$40",
        "duración": "cuatro días y 3 noches",
        "caminata": "es un paseo en el cerro"
    },
     {
        "ciudad": "Medellín",
        "nombre": "TourMedellín",
        "precio": "$410",
        "duración": "3 dias",
        "transporte": "privado",
        "caminata": "jardin botanico, parque explora, museo de arte moderno, comuna 13, seguro contra accidentes y asistencia medica",
    },
    {
        "ciudad": "Cartagena",
        "precio": "$400",
        "duración": "2 días y 1 noche",
        "caminata": "es un paseo"
    },
]

idVuelos = 1 

while True:
    print("\n---\n Bienvenido a la agencia de vuelos----")
    print("1. A donde quieres ir?")
    print("2. Modificar mi vuelo")
    print("3. Eliminar mi vuelo")
    print("4. Mostrar mis reservas")
    print("5. salir")

    opcion = input("Elige la opción deseada: ")

    # Haciendo reservas
    if opcion == "1":
        origen = input("¿Cuál es tu origen?: ")
        destino = input("Escribe su destino: ")
        pasajeros = input("Cantidad de pasajeros en números: ")
        fecha_Ida = input("Ingrese fecha de ida (dd/mm/aaaa): ")
        fecha_Regreso = input("Ingrese fecha de regreso (dd/mm/aaaa): ")

        listaVuelos.append({
            "id": idVuelos, 
            "origen": origen, 
            "destino": destino, 
            "pasajeros": pasajeros, 
            "fecha de ida": fecha_Ida, 
            "fecha de regreso": fecha_Regreso
        })

        print("\n---\n Escoge tu vuelo ---")
        if listaVuelos[0]["destino"].lower() == "medellin":
            for i, viaje in enumerate(viajes, start=1):  # Comienza la numeración en 1
                if viaje["ciudad"].lower() == "medellín":
                    print(f"{i}. Ciudad: {viaje['ciudad']}")
                    print(f"   Precio: {viaje['precio']}")
                    print(f"   Duración: {viaje['duración']}")
                    print(f"   Caminata: {viaje['caminata']}")
                    print()  # Espacio adicional entre los viajes
            


            opcionViajesMedellin = input("Escoge tu vuelo (número): ")
            if int(opcionViajesMedellin) == 1:
                listaVuelos[0].update(viajes[0])  # Combina los datos
                print("\n¡Vuelo añadido exitosamente!")
                print(f"Detalles del vuelo: {listaVuelos[0]}")  # Muestra el objeto actualizado

            if int(opcionViajesMedellin) == 2:
                listaVuelos[0].update(viajes[1])  # Combina los datos
                print("\n¡Vuelo añadido exitosamente!")
                print(f"Detalles del vuelo: {listaVuelos[0]}")  # Muestra el objeto actualizado   

        elif listaVuelos[0]["destino"].lower() == "cartagena":
              for i, viaje in enumerate(viajes, start=1):  # Comienza la numeración en 1
                if viaje["ciudad"].lower() == "cartagena":
                    print(f"{i}. Ciudad: {viaje['ciudad']}")
                    print(f"   Precio: {viaje['precio']}")
                    print(f"   Duración: {viaje['duración']}")
                    print(f"   Caminata: {viaje['caminata']}")
                    print()  # Espacio adicional entre los viajes

                opcionViajesCartagena = input("Escoge tu vuelo (número): ")
                if int(opcionViajesCartagena) == 1:
                    listaVuelos[0].update(viajes[3]) 
                    print("\n¡Vuelo añadido exitosamente!")
                    print(f"Detalles del vuelo: {listaVuelos[0]}")  
        idVuelos += 1

# Modificar vuelo
    elif opcion == "2":
        vuelo_encontrado = False
        idActualizar = int(input("Ingrese el ID del vuelo que quiere actualizar: "))
        
        for vuelo in listaVuelos:
            if vuelo["id"] == idActualizar:
                nuevoOrigen = input("Ingrese el nuevo origen (dejar en blanco si no quiere modificarlo): ")
                nuevoDestino = input("Ingrese el nuevo destino (dejar en blanco si no quiere modificarlo): ")
                nuevosPasajeros = input("Ingrese la nueva cantidad de pasajeros (dejar en blanco si no quiere modificarla): ")
                nuevaFechaIda = input("Ingrese una nueva fecha (dejar en blanco si no quiere modificarla): ")
                nuevaFechaRegreso = input("Ingrese una nueva fecha (dejar en blanco si no quiere modificarla): ")

                if nuevoOrigen:
                    vuelo["origen"] = nuevoOrigen
                if nuevoDestino:
                    vuelo["destino"] = nuevoDestino
                if nuevosPasajeros:
                    vuelo["pasajeros"] = nuevosPasajeros
                if nuevaFechaIda:
                    vuelo["fecha de ida"] = nuevaFechaIda
                if nuevaFechaRegreso:
                    vuelo["fecha de regreso"] = nuevaFechaRegreso

                print(f"Vuelo {idActualizar} actualizado con éxito.\n")
                vuelo_encontrado = True
                break
        
        if not vuelo_encontrado:
            print(f"No se encontró el vuelo con el ID: {idActualizar}\n")

    # Eliminar reserva
    elif opcion == "3":
        idEliminar = int(input("Ingrese el ID a eliminar: "))
        vuelo_encontrado = False
        for vuelo in listaVuelos:
            if vuelo["id"] == idEliminar:  
                listaVuelos.remove(vuelo) 
                print(f"Vuelo {idEliminar} eliminado exitosamente.")
                vuelo_encontrado = True
                break
        
        if not vuelo_encontrado:
            print(f"No se encontró el vuelo con el ID {idEliminar}")

    # Mostrar reservas
    elif opcion == "4":
        if len(listaVuelos) == 0:
            print("No hay vuelos reservados.")
        else:
            print("- LISTA DE VUELOS -")
            for vuelo in listaVuelos:
                print(f"ID: {vuelo['id']} | Origen: {vuelo['origen']} | Destino: {vuelo['destino']} | Pasajeros: {vuelo['pasajeros']} | Fecha de Ida: {vuelo['fecha de ida']} | Fecha de Regreso: {vuelo['fecha de regreso']}")
            print()

    # Salir
    elif opcion == "5":
        print("Muchas gracias por su visita")
        break

    else:
        print("Opción inválida, por favor verifique.")

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






        