from baraja import *

class Mesa:
   
   def __init__(self, baraja):
      self.mazo=Carta.cargarCartas(baraja)
      print(len(self.mazo))
      self.cartaSobre=[]

   def mezclar(self):
      self.mazo=Carta.mezclar(self.mazo)
   
   def ponerCarta(self,carta):
      self.cartaSobre.append(carta)

   def numeroCartasBaraja(self):
      return len(self.mazo)

   def mostrarMesa(self,seleccion=False):
      for i,carta in enumerate(self.cartaSobre):
         carta.mostrar(((i+1) if seleccion else None))
   
   def numeroCartasEnMesa(self):
      return len(self.cartaSobre)
   
   def robar(self):
      return self.mazo.pop(0)