import random as rd
class Cartas:
   ESPAÑOLA40   =  0
   FRANCESA52   =  1
class Carta:
   def __init__(self,etiqueta,valor,palo):
      self.etiqueta = etiqueta
      self.valor = valor
      self.palo = palo
   @staticmethod
   def cargarCartas(tipoBaraja):
      #Carga el fichero con la definición de cada carta y su valor

      baraja=[]
      if(tipoBaraja==Cartas.ESPAÑOLA40):
         for p in ['Oros',"Copas","Espadas", "Bastos"]:
            baraja.append(Carta("As " +p,1,p))
            for i in range(2,7): #7 para 40, 10 para 48 o 11 para 52
               baraja.append(Carta(str(i)+" " +p,i,p))
            baraja.append(Carta("Sota " +p,10,p))
            baraja.append(Carta("Caballo " +p,11,p))
            baraja.append(Carta("Rey " +p,12,p))
      elif tipoBaraja==Cartas.FRANCESA52:
         for p in ['Corazones',"Diamantes","Picas", "Treboles"]:
            baraja.append(Carta("As " +p,1,p))
            for i in range(2,11): #7 para 40, 10 para 48 o 11 para 52
               baraja.append(Carta(str(i)+" " +p,i,p))
            baraja.append(Carta("J "+p, "J",p))
            baraja.append(Carta("Q "+p, "Q",p))
            baraja.append(Carta("K "+p, "K",p))

      return baraja
   @staticmethod
   def mezclar(mazo):
      rd.shuffle(mazo)
      return mazo


   def mostrar(self,numeracion=None):
      print((str(numeracion)+". " if numeracion!=None else "")+self.etiqueta)
   