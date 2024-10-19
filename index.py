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

listaPaquetesTuristicos = [
    {
        "nombre": "TourMedellín",
        "duracion": "3 días",
        "transporte": "privado",
        "actividades": "jardín botánico, parque explora, museo de arte moderno, comuna 13",
        "seguridad": "seguro contra accidentes y asistencia médica"
    },
    {
        "nombre": "MedalloExtremo",
        "duracion": "tres días y dos noches",
        "transporte": "privado",
        "actividades": "parapente en guatapé, visita a las cascadas de san luis, recorrido en cuatrimotos",
        "seguridad": "seguro contra accidentes y asistencia médica"
    },
    {
        "nombre": "CartagenaBeach",
        "duracion": "12 horas",
        "transporte": "terrestre privado, lancha rápida",
        "actividades": "excursión Bora Bora Beach, Isabella y Pao Pao Beach.",
        "alimentacion": "cóctel de bienvenida, almuerzo, refrigerio, agua y gaseosa en la lancha",
        "seguridad": "seguro contra accidentes y asistencia médica"
    },
]

Listadehoteles = [
    {
        "nombre": "Hotel Medellín Royal",
        "ciudad": "Medellín",
        "tipo_habitacion": "Individual/Múltiple",
        "descripcion": "Moderno y bien ubicado, con buenas comodidades y desayuno incluido.",
        "precio": "80.000 pesos"
    },
    {
        "nombre": "The Charlee Hotel",
        "ciudad": "Medellín",
        "tipo_habitacion": "Individual/Múltiple",
        "descripcion": "Hotel boutique en El Poblado, conocido por su ambiente vibrante y vistas a la ciudad.",
        "precio": "100.000 pesos"
    },
    {
        "nombre": "Hotel Nutibara",
        "ciudad": "Medellín",
        "tipo_habitacion": "Individual/Múltiple",
        "descripcion": "Hotel tradicional en el centro de Medellín, con fácil acceso a lugares turísticos.",
        "precio": "50.000 pesos"
    },
    {
        "nombre": "Hotel Casa San Agustín",
        "ciudad": "Cartagena",
        "tipo_habitacion": "Individual/Múltiple",
        "descripcion": "Elegante hotel en el centro histórico, combina estilo colonial con comodidades modernas.",
        "precio": "150.000 pesos"
    },
    {
        "nombre": "Hotel Caribe",
        "ciudad": "Cartagena",
        "tipo_habitacion": "Individual/Múltiple",
        "descripcion": "Hotel clásico frente a la playa, ideal para relajarse y disfrutar del mar.",
        "precio": "120.000 pesos"
    },
    {
        "nombre": "Hostal Casa La Fe",
        "ciudad": "Cartagena",
        "tipo_habitacion": "Individual/Múltiple",
        "descripcion": "Hostal acogedor en el corazón de Cartagena, perfecto para viajeros jóvenes.",
        "precio": "30.000 pesos"
    },
]

idVuelos = 1

while True:
    print("\n---\n Bienvenido a la agencia de viajes y paquetes turísticos ----")
    print("1. Reservar un vuelo")
    print("2. Modificar mi vuelo")
    print("3. Eliminar mi vuelo")
    print("4. Mostrar mis reservas")
    print("5. Salir")
    
    opcion = input("Elige la opción deseada: ")
    
    # Haciendo reservas de vuelos
    if opcion == "1":
        origen = input("¿Cuál es tu origen?: ")
        destino = input("Escribe su destino: ")
        pasajeros = input("Cantidad de pasajeros en números: ")
        fecha_Ida = input("Ingrese fecha de ida (dd/mm/aaaa): ")
        fecha_Regreso = input("Ingrese fecha de regreso (dd/mm/aaaa): ")
        
        vuelo = {
            "id": idVuelos,
            "origen": origen,
            "destino": destino,
            "pasajeros": pasajeros,
            "fecha de ida": fecha_Ida,
            "fecha de regreso": fecha_Regreso
        }
        
        # Escoger paquete turístico
        print("\n---\n Escoge un paquete turístico ---")
        for i, paquete in enumerate(listaPaquetesTuristicos, start=1):
            print(f"{i}. Nombre: {paquete['nombre']}")
            print(f"   Duración: {paquete['duracion']}")
            print(f"   Transporte: {paquete['transporte']}")
            print(f"   Actividades: {paquete['actividades']}")
            print(f"   Seguridad: {paquete['seguridad']}\n")
            
        opcionPaquete = int(input("Escoge tu paquete turístico (número): "))
        vuelo["paquete turistico"] = listaPaquetesTuristicos[opcionPaquete - 1]

        # Escoger hotel
        print("\n---\n Escoge un hotel ---")
        for i, hotel in enumerate(Listadehoteles, start=1):
            print(f"{i}. Nombre: {hotel['nombre']}")
            print(f"   Ciudad: {hotel['ciudad']}")
            print(f"   Tipo habitación: {hotel['tipo_habitacion']}")
            print(f"   Descripción: {hotel['descripcion']}")
            print(f"   Precio: {hotel['precio']}\n")
        
        opcionHotel = int(input("Escoge tu hotel (número): "))
        vuelo["hotel"] = Listadehoteles[opcionHotel - 1]

        # Añadir vuelo a la lista de reservas
        listaVuelos.append(vuelo)
        print("\n¡Reserva realizada exitosamente!")
        print(f"Detalles de tu reserva: {vuelo}")  # Imprime la información de la reserva
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
                print(f"   Paquete Turístico: {vuelo['paquete turistico']['nombre']}")
                print(f"   Hotel: {vuelo['hotel']['nombre']}\n")

    # Salir de la agencia
    elif opcion == "5":
        print("Muchas gracias por su visita")
        break
    else:
        print("Opción inválida, por favor verifique.")
