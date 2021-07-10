

class Jugador:
   def __init__(self,nombre,esBot):
      self.nombre = nombre
      self.esBot=esBot
      self.mano=[]
      self.cuenta=[]
      self.puntuacion=0
      

   def ponerMano(self, mano):
      self.mano=mano
   
   def cogerCarta(self, carta):
      self.mano.append(carta)
   def poseeValorCarta(self, valor):
      for i,carta in enumerate(self.mano):
         if carta.valor==valor:
            return i
      return -1
   def ponerCartaCuenta(self, carta):
      self.cuenta.append(carta)
   def mostrarMano(self,seleccion=False):
      for i,carta in enumerate(self.mano):
         carta.mostrar(((i+1) if seleccion else None))
   
   def mostrarCuenta(self):
      print("Valores en cuenta")
      for carta in self.cuenta:
         carta.mostrar()
   def sumarPuntuacion(self, valor):
      self.puntuacion+=valor
   def ponerPuntuacion(self):
      self.puntuacion=0
   def obtenerPuntuacion(self):
      return self.puntuacion
   def numeroCartasEnMano(self):
      return len(self.mano)
   def esHumano(self):
      return not self.esBot