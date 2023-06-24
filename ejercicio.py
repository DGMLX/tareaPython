# OTRAS CONSIDERACIONES:
# • Los datos se deben almacenar en arreglos.
# • El sistema debe realizar todas las validaciones necesarias en el ingreso de datos.


import funciones as fn
import numpy as np
from colorama import Fore,init
init()


opcion = 0
matrizMapa = np.array([[Fore.WHITE +"F",Fore.GREEN +"00","00","00","00","00",Fore.BLUE + "00","00","00","00",Fore.RED +"00","00",Fore.GREEN +"00",Fore.BLUE +"00","00","00","00","00","00","00","00","00","00","00","00","00","00","00"],[Fore.WHITE +"E",Fore.GREEN +"00","00","00","00","00",Fore.BLUE + "00","00","00","00",Fore.RED +"00","00",Fore.GREEN +"00",Fore.BLUE +"00","00","00","00","00","00","00","00","00","00","00","00","00","00","00"],[Fore.WHITE +"D",Fore.GREEN +"00","00","00","00","00",Fore.BLUE + "00","00","00","00",Fore.RED +"00","00",Fore.GREEN +"00",Fore.BLUE +"00","00","00","00","00","00","00","00","00","00","00","00","00","00","00"],[" ",Fore.WHITE+ "01","02","03","04","05","06","07","08","09","10","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33"],[Fore.WHITE +"C",Fore.GREEN +"00","00","00","00","00",Fore.BLUE + "00","00","00","00",Fore.RED +"00","00",Fore.GREEN +"00",Fore.BLUE +"00","00","00","00","00","00","00","00","00","00","00","00","00","00","00"],[Fore.WHITE +"B",Fore.GREEN +"00","00","00","00","00",Fore.BLUE + "00","00","00","00",Fore.RED +"00","00",Fore.GREEN +"00",Fore.BLUE +"00","00","00","00","00","00","00","00","00","00","00","00","00","00","00"],[Fore.WHITE +"A",Fore.GREEN +"00","00","00","00","00",Fore.BLUE + "00","00","00","00",Fore.RED +"00","00",Fore.GREEN +"00",Fore.BLUE +"00","00","00","00","00","00","00","00","00","00","00","00","00","00","00"]])

filas = []
columnas = []
rutPasajeros = []
asientoComun = []
asientoNoReclina = []
asientoPiernas = []

while opcion != 7:
    fn.generarMenu()
    try:
        opcion = int(input("Escoga una opción: "))
        if opcion > 0 and opcion < 8:
            if opcion == 1:
                fn.comprarPasajes(matrizMapa,filas,columnas,rutPasajeros,asientoComun,asientoNoReclina,asientoPiernas)
            elif opcion == 2:
                fn.mostrarMapa(matrizMapa)
            elif opcion == 3:
                fn.verListadoPasajeros(rutPasajeros)
            elif opcion == 4:
                fn.buscarPasajero(rutPasajeros)
            elif opcion == 5:
                fn.reasignarAsiento(rutPasajeros)
            elif opcion == 6:
                fn.mostrarGanancias(asientoComun,asientoNoReclina,asientoPiernas)
            else:
                print("Has salido del programa")
        else:
            print("Ingrese una opción dentro del rango.")
    except:
        print("ERROR, Ingrese un valor numérico. ")
    
