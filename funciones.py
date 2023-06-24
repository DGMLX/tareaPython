import numpy as np
from colorama import Fore,init
init()

def generarMenu():
    itemsMenu = [Fore.WHITE +"Comprar pasajes","Mostrar ubicaciones disponibles","Ver listado de pasajeros","Buscar pasajero","Reasignar asiento","Mostrar ganancias totales","Salir"]
    for x in range(len(itemsMenu)):
        print(f"{x+1}) {itemsMenu[x]}")

def comprarPasajes(matrizMapa,filas,columnas,rutPasajeros,asientoComun,asientoPiernas,asientoNoReclina):
    while True:
        try:
            cantPasajes = int(input("¿Cuantos pasajes desea comprar?: "))
            if cantPasajes > 0 and cantPasajes < 199:
                acum = 0
                # mostrarMapa(matrizMapa)
                print(Fore.WHITE +" ")
                while acum != cantPasajes:
                    opcion = 0
                    while opcion !=1:
                        while True:
                            mostrarMapa(matrizMapa)
                            try:
                                fila = input(Fore.WHITE + "Selecciona la fila en la que desea estar: ")
                                fila = fila.upper()
                                validacion = validarFila(fila)
                                if validacion == True:

                                    
                                    break
                                else:
                                    print("Fila inválida.")
                            except:
                                print("Ingresa un valor válido.")
                        while True:
                            try:
                                columna = int(input("Seleccione la columna en la que desea estar: "))
                                if columna > 0 and columna < 34:
                                    columna = str(columna)
                                    if len(columna) == 1:
                                        columna = "0"+columna
                                    rangosColumnas = validarColumna(columna,asientoPiernas,asientoNoReclina,asientoComun)
                                    if rangosColumnas == True:
                                        break
                                    else:
                                        print("Ingresa una columna dentro del rango.")
                                else:
                                    print("Valor columna fuera de rango.") 
                            except:
                                print("Ingrese valor numérico.")
                        
                        # print(fila,columna,filas,columnas)

                        while True:
                            validaUbicacionColumna = False
                            validaUbicacionFila = False
                            if len(filas)>0:
                                for x in range(len(filas)):
                                    if fila == filas[x]:
                                        validaUbicacionFila = True
                                for y in range(len(columnas)):
                                    if columna == columnas[y]:
                                        validaUbicacionColumna = True
                                if validaUbicacionFila == True and validaUbicacionColumna == True:
                                    print("ubicacion ocupada, porfavor ingrese otra ubicación.")
                                    break
                                else:
                                    filas.append(fila)
                                    columnas.append(columna)
                                    opcion = 1
                                    break
                            else:
                                filas.append(fila)
                                columnas.append(columna)
                                opcion = 1
                                break

                                    
                    actualizarMapa(fila,columna,matrizMapa)
                    while True:
                        try:
                            rut = int(input("Ingrese rut del pasajero sin puntos ni digito verificador: "))
                            # rut = str(rut)
                            if rut > 9999999 and rut <100000000:
                                validacionRut = validarRut(rut,rutPasajeros)
                                if validacionRut == True:
                                    rutPasajeros.append(rut)
                                    break
                                else:
                                    print("Debe ingresar otro RUT, el ingresado ya se encuentra en el sistema.")
                            else:
                                print("Rut fuera de rango.")
                        except:
                            print("Ingrese un rut con valores válidos.")
                    acum += 1
                    print("Pasajero guardado correctamente.")
                print("Todos los pasajes han sido guardados en el sistema.")
                print(rutPasajeros)
                #print(filas,columnas,rutPasajeros)
                    
                break
            else:
                print("ERROR. Debe ingresar un valor mayor a 0 y menor a 199.")
        except:
            print("ERROR. Ingresa un valor numérico.")

def mostrarMapa(matrizMapa):
    print("-"*40,"UBICACIONES","-"*40)
    print(" ")
    for x in range(len(matrizMapa)):
        for i in range(len(matrizMapa[0])):
                print(matrizMapa[x][i],end=" ")
                if i == 27:
                    print("\n")

def validarFila(fila):
    valoresFilas = ["A","B","C","D","E","F"]
    for x in valoresFilas:
        if fila == x:
            return True
        
def validarRut(rut,rutPasajeros):
    validacion = False
    for x in range(len(rutPasajeros)):
        if rut == rutPasajeros[x]:
            validacion = True
    if validacion == True:
        return False
    else:
        return True

        

def validarColumna(columna,asientoComun,asientoPiernas,asientoNoReclina):
    columna = int(columna)
    if (columna> 0 and columna <6) or columna == 18:
        asientoPiernas.append(1)
        return True
    elif (columna >5 and columna < 10) or (columna > 18 and columna < 34):
        asientoComun.append(1)
        return True
    elif columna == 10 or columna == 17:
        asientoNoReclina.append(1)
        return True
    else:
        return False
def verListadoPasajeros(rutPasajeros):
    print("*"*20, "LISTADO DE PASAJEROS","*"*20)
    if len(rutPasajeros) == 0:
        print("No hay pasajeros en el sistema.")
    else:
        rutPasajeros.sort()
        for x in range(len(rutPasajeros)):
            print(f"{x+1}) {rutPasajeros[x]}")
    print("*"*62)

def actualizarMapa(fila,columna,matrizMapa):
    for x in range(len(matrizMapa)):
        if matrizMapa[x][0] == Fore.WHITE + fila:
            valorFila = x
            validacionFila = True
            # print("coincide fila")

    for y in range(len(matrizMapa[3])):
        if columna == "01":
            if matrizMapa[3][y] == Fore.WHITE + columna:
                valorColumna = y
                validacionColumna = True
                # print("coincide columna")
        elif matrizMapa[3][y] == columna:
            valorColumna = y
            validacionColumna = True
            # print("coincide columna")
    if validacionColumna == True and validacionFila == True:
        # print([valorFila,valorColumna])
        matrizMapa[valorFila,valorColumna] = "XX"
        
def buscarPasajero(rutPasajeros):
    if len(rutPasajeros) == 0:
        print("Por el momento no hay pasajeros en el sistema.")
    else:
        while True:
            try:
                validar = False
                rutFiltrar = int(input("Ingrese rut para buscar pasajero: "))
                # rutFiltrar = str(rutFiltrar)
                if rutFiltrar > 9999999 and rutFiltrar < 100000000:
                    for x in rutPasajeros:
                        if x == rutFiltrar:
                            validar = True
                    if validar == True:
                        print("El Rut si esta en la lista de pasajeros.")
                    else:
                        print("El Rut no se encuentra en la lista de pasajeros.")
                    break
                else:
                    print("Ingrese un rut válido.")
            except:
                print("Ingrese valores numéricos.")
    
def reasignarAsiento(rutPasajeros):
    if len(rutPasajeros) == 0:
        print("Por el momento no hay pasajeros en el sistema.")
    else:
        while True:
            while True:
                try:
                    rutAntiguoPasajero = int(input("Ingrese rut del antiguo pasajero para reasignar el asiento: "))
                    # rutAntiguoPasajero = str(rutAntiguoPasajero)
                    if rutAntiguoPasajero > 9999999 and rutAntiguoPasajero < 100000000:
                        print(rutPasajeros)
                        print(rutAntiguoPasajero)

                        for x in rutPasajeros:
                            if rutAntiguoPasajero == x:
                                valido = True
                        if valido == True:
                            while True:
                                try:
                                    rutNuevoPasajero = int(input("Ingrese rut del nuevo pasajero: "))
                                    # rutNuevoPasajero = str(rutNuevoPasajero)
                                    if rutNuevoPasajero > 9999999 and rutNuevoPasajero < 100000000:
                                        validacionNuevoPasajero = validarNuevaUbicacion(rutNuevoPasajero,rutPasajeros)
                                        if validacionNuevoPasajero == True:
                                            print("Debe ingresar otro número de rut, este ya se encuentra en el sistema.")
                                        else:
                                            for x in range(len(rutPasajeros)):
                                                if rutPasajeros[x] == rutAntiguoPasajero:
                                                    rutPasajeros[x] = rutNuevoPasajero
                                            print("Asiento reasignado correctamente")
                                            break
                                    else:
                                        print("Ingrese un rut válido.")
                                except:
                                    print("Ingrese valores numéricos.")
                                
                        
                        # for x in range(len(rutPasajeros)):
                        #     if rutAntiguoPasajero == rutPasajeros[x]:
                        #         valido = True
                        #         indiceRut = x
                        #     else:
                        #         valido = False
                        # if valido == True:
                        #     while True:
                        #         try:
                        #             rutNuevoPasajero = int(input("Ingrese rut del nuevo pasajero: "))
                        #             # rutNuevoPasajero = str(rutNuevoPasajero)
                        #             if rutNuevoPasajero > 9999999 and rutNuevoPasajero < 100000000:
                        #                 rutPasajeros[indiceRut] = rutNuevoPasajero
                        #                 print("Asiento reasignado correctamente")
                        #                 break
                        #             else:
                        #                 print("Ingrese un rut válido.")
                        #         except:
                        #             print("Ingrese valores numéricos.")

                        else:
                            print("El rut ingresado no se encuentra en la lista de pasajeros.")
                        
                    else:
                        print("Ingrese un rut válido.")
                    break
                except:
                    print("Ingrese valores numéricos.")
            break

def validarNuevaUbicacion(rutNuevoPasajero,rutPasajeros):
    for x in range(len(rutPasajeros)):
        if rutNuevoPasajero == rutPasajeros[x]:
            return True
        else:
            return False

            
def mostrarGanancias(asientoComun,asientoNoReclina,asientoPiernas):
    print("-"*80)
    print("TIPO DE ASIENTO", " "*30,"CANTIDAD"," "*20,"TOTAL")
    print(f"Asiento comun"," "*9,"$60.000", " "*18,len(asientoComun)," "*25,f"${len(asientoComun)*60000}")
    print("Espacio para piernas"," "*2,"$80.000"," "*18,len(asientoPiernas)," "*25,f"${len(asientoPiernas)*80000}")
    print(f"No reclina"," "*12,"$50.000"," "*18,len(asientoNoReclina)," "*25,f"${len(asientoNoReclina)*50000}")
    print(f"Total"," "*44,len(asientoComun)+len(asientoNoReclina)+len(asientoPiernas)," "*25,f"${len(asientoComun)*60000 + len(asientoPiernas)*80000 + len(asientoNoReclina)*50000}")
    print("-"*80)