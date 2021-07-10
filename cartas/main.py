import juegoCasino
from utilidades import *


print("Juego de Cartas hecho en Python")
juego=juegoCasino.Juego()
while not juego.terminado():
   juego.ronda()
ganadores=juego.obtenerGanador()
if(len(ganadores)>1):
   print(Colores.BOLD+"LOS GANADORES SON"+Colores.END)
   for ganador in ganadores:
      print(Colores.RED+ganador.nombre+Colores.END)
else:
   print(Colores.BOLD+"EL GANADOR ES"+Colores.END)
   print(Colores.RED+ganadores[0].nombre+Colores.END)