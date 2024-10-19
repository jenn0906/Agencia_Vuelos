
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
        "duración": "3 días",
        "transporte": "privado",
        "caminata": "jardín botánico, parque explora, museo de arte moderno, comuna 13, seguro contra accidentes y asistencia médica",
    },
    {
        "ciudad": "Cartagena",
        "precio": "$400",
        "duración": "2 días y 1 noche",
        "caminata": "es un paseo"
    },
]

idVuelos = 1
usuarios = []  # Lista para almacenar usuarios registrados

while True:
    print("\n---\n Bienvenido a la agencia de vuelos ----")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. A dónde quieres ir?")
    print("4. Modificar mi vuelo")
    print("5. Eliminar mi vuelo")
    print("6. Mostrar mis reservas")
    print("7. Salir")

    opcion = input("Elige la opción deseada: ")

    if opcion == "1":  # Registro de usuario
        correo = input("Ingrese su correo electrónico: ")
        telefono = input("Ingrese su número de teléfono: ")
        usuarios.append({"correo": correo, "telefono": telefono})
        print(f"Usuario registrado con éxito. Correo: {correo}, Teléfono: {telefono}")

    elif opcion == "2":  # Iniciar sesión
        correo = input("Ingrese su correo electrónico: ")
        telefono = input("Ingrese su número de teléfono: ")
        
        # Verificar si el usuario existe
        usuario_encontrado = False
        for usuario in usuarios:
            if usuario["correo"] == correo and usuario["telefono"] == telefono:
                print("Inicio de sesión exitoso.")
                usuario_encontrado = True
                break
        
        if not usuario_encontrado:
            print("Credenciales incorrectas. Intente nuevamente.")

    elif opcion == "3":  # Haciendo reservas
        if not usuario_encontrado:
            print("Debes iniciar sesión para hacer una reserva.")
            continue
        
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
            "fecha de regreso": fecha_Regreso,
            "correo": correo,
            "telefono": telefono
        })

        print("\n---\n Escoge tu vuelo ---")
        if listaVuelos[0]["destino"].lower() == "medellín":
            for i, viaje in enumerate(viajes, start=1):
                if viaje["ciudad"].lower() == "medellín":
                    print(f"{i}. Ciudad: {viaje['ciudad']}")
                    print(f"   Precio: {viaje['precio']}")
                    print(f"   Duración: {viaje['duración']}")
                    print(f"   Caminata: {viaje['caminata']}")
                    print()

            opcionViajesMedellin = input("Escoge tu vuelo (número): ")
            if int(opcionViajesMedellin) == 1:
                listaVuelos[0].update(viajes[0])
                print("\n¡Vuelo añadido exitosamente!")
                print(f"Detalles del vuelo: {listaVuelos[0]}")

            if int(opcionViajesMedellin) == 2:
                listaVuelos[0].update(viajes[1])
                print("\n¡Vuelo añadido exitosamente!")
                print(f"Detalles del vuelo: {listaVuelos[0]}")

        elif listaVuelos[0]["destino"].lower() == "cartagena":
            for i, viaje in enumerate(viajes, start=1):
                if viaje["ciudad"].lower() == "cartagena":
                    print(f"{i}. Ciudad: {viaje['ciudad']}")
                    print(f"   Precio: {viaje['precio']}")
                    print(f"   Duración: {viaje['duración']}")
                    print(f"   Caminata: {viaje['caminata']}")
                    print()

            opcionViajesCartagena = input("Escoge tu vuelo (número): ")
            if int(opcionViajesCartagena) == 1:
                listaVuelos[0].update(viajes[2])
                print("\n¡Vuelo añadido exitosamente!")
                print(f"Detalles del vuelo: {listaVuelos[0]}")

        idVuelos += 1

    elif opcion == "4":  # Modificar vuelo
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

    elif opcion == "5":  # Eliminar reserva
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

    elif opcion == "6":  # Mostrar reservas
        if len(listaVuelos) == 0:
            print("No hay vuelos reservados.")
        else:
            print("- LISTA DE VUELOS -")
            for vuelo in listaVuelos:
                print(f"ID: {vuelo['id']} | Origen: {vuelo['origen']} | Destino: {vuelo['destino']} | Pasajeros: {vuelo['pasajeros']} | Fecha de Ida: {vuelo['fecha de ida']} | Fecha de Regreso: {vuelo['fecha de regreso']} | Correo: {vuelo['correo']} | Teléfono: {vuelo['telefono']}")
            print()

    elif opcion == "7":  # Salir
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






        