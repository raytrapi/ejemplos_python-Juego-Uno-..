import random as rd


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def crearBaraja():
   baraja=[]
   for v in range(0,9):
      for color in colores[1:]:
         for _ in range(2 if v>0 else 1):
            baraja.append({"color":color,"valor":str(v), "robar":0})

   for _ in range(4): #Añadimos las cartas especiales
      baraja.append({"color":"NEGRO", "valor":"+4", "robar":4})
      baraja.append({"color":"NEGRO", "valor":"COMODIN", "robar":0})

   for _ in range(3): #Añadimos las cartas de +2
      for color in colores[1:]:
         baraja.append({"color":color, "valor":"+2", "robar":2})
         baraja.append({"color":color, "valor":"CAMBIO", "robar":0})
         baraja.append({"color":color, "valor":"SALTO", "robar":0})
   rd.shuffle(baraja)
   return baraja



def pintarCarta(carta):
   return ((carta["color"]+" ") if carta["color"]!="NEGRO" else "") +carta["valor"] + ("("+str(carta["robar"])+")" if carta["robar"]>0 else "")

def cumpleLasReglas(cartaEscogida,cartaEnMesa):
   if cartaEscogida["color"]=="NEGRO":
      return True
   else:
      return cartaEnMesa["color"]==cartaEscogida["color"] or cartaEnMesa["valor"]==cartaEscogida["valor"]
def mostrarMano(jugador, numeradas=False,cartaMesa=None):
   i=1
   col=0
   cadenaSalida=""
   for carta in jugador["mano"]:
      
      textoCarta=((str(i)+" " if numeradas else ""))
      if cartaMesa!=None and cumpleLasReglas(carta,cartaMesa):
         textoCarta+=bcolors.BOLD+ pintarCarta(carta)+bcolors.ENDC
      else:
         textoCarta+=pintarCarta(carta)
      cadenaSalida+=("\t" if col>0 else "\r\n")+textoCarta.ljust(20," ")
      if(col==3):
         col=0
      else:
         col+=1
      i+=1
   print(cadenaSalida)
def escogerColor():
   colorEscogido=""
   repetir=True
   while repetir:
      i=1
      for color in colores[1:]:
         print(str(i)+" "+color)
         i+=1
      colorEscogido=input("Escoge color: ")
      if colorEscogido.isnumeric() and int(colorEscogido)>0 and int(colorEscogido) <= len(colores)-1:
         repetir=False
   return colores[int(colorEscogido)]
def robar(jugador,numero,baraja):
   for _ in range(numero):
      if len(baraja)>0:
         jugador["mano"].append(baraja[0])
         baraja=baraja[1:]
   return baraja

def controlaRobos(jugador,cartaMesa,baraja):
   if cartaMesa["valor"]=="+4":
      #Tengo que robar 4 cartas
      print(bcolors.FAIL +"\t---ROBA 4 Cartas---" + bcolors.ENDC)
      baraja=robar(jugador,4,baraja)
      cartaMesa["robar"]=0
   elif cartaMesa["valor"]=="+2" and cartaMesa["robar"]>0:
      tengo=False
      for carta in jugador["mano"]:
         tengo=tengo or carta["valor"]=="+2"
      if not tengo:
         print(bcolors.FAIL +"\t---ROBA "+str(cartaMesa["robar"])+" Cartas---" + bcolors.ENDC)
         baraja=robar(jugador, cartaMesa["robar"],baraja)
         cartaMesa["robar"]=0
   return baraja
def escogerCarta(jugador, cartaEnMesa, baraja):
   #Pintamos la mano
   repetir=True
   selecioniada=None

   while repetir:
      mostrarMano(jugador, True, cartaEnMesa)
      print("\r\nCarta en la mesa: ", pintarCarta(monton[-1]))
      idCartaEscogida=input("Que carta quieres tirar (R para robar "+str(len(baraja))+"):").capitalize()
      if idCartaEscogida=="R":
         if len(baraja)>0:
            baraja=robar(jugador,1,baraja)
         else:
            print("NO HAY CARTAS PARA ROBAR")
      elif idCartaEscogida.isnumeric() and int(idCartaEscogida)>0 and int(idCartaEscogida)<=len(jugador["mano"]):
         cartaEscogida=jugador["mano"][int(idCartaEscogida)-1]
         if cumpleLasReglas(cartaEscogida,cartaEnMesa):
            jugador["mano"]=jugador["mano"][0:int(idCartaEscogida)-1]+jugador["mano"][int(idCartaEscogida):]
            if(cartaEscogida["color"]=="NEGRO"):
               cartaEscogida["color"]=escogerColor()
            repetir=False
         else:
            print("ESA CARTA NO VALE")
   return cartaEscogida,baraja

def jugarCarta(jugador, cartaEnMesa, baraja):
   #Pintamos la mano
   repetir=True
   selecioniada=None
   while repetir:
      #mostrarMano(jugador, True) #Lo quitaríamos despues para evitar que los usuario lo vean
      #print("\r\n\r\nCarta en la mesa: ", pintarCarta(monton[-1]))
      print("Tiene "+str(len(jugador["mano"]))+" cartas")
      
      cartasValidas=[]
      cartasColor={}
      for i,carta in enumerate(jugador["mano"]):
         if cumpleLasReglas(carta,cartaEnMesa):
            cartasValidas.append(i)
         if carta["color"]!="NEGRO":
            if carta["color"] in cartasColor:
               cartasColor[carta["color"]]+=1
            else:
               cartasColor[carta["color"]]=1

      #Sabemos que cartas son válidas
      idCartaSeleccionada=-1
      if len(cartasValidas)==0:
         if len(baraja)>0:
            print(bcolors.WARNING+"\tRobo carta"+bcolors.ENDC)
            baraja=robar(jugador,1,baraja)
         else:
            print("NO HAY CARTAS PARA ROBAR")
            #TODO: Definir que pasa cuando ya no hay carta
            return None,baraja
      else:
         #Cogemos la más ventajosa
         for idCarta in cartasValidas:
            if idCartaSeleccionada<0:
               idCartaSeleccionada=idCarta
            else:
               if not jugador["mano"][idCarta]["valor"].isnumeric():
                  idCartaSeleccionada=idCarta
      
         if jugador["mano"][idCartaSeleccionada]["color"]=="NEGRO":
            color=""
            colorNumero=0
            for c in cartasColor:
               if cartasColor[c]>colorNumero:
                  colorNumero=cartasColor[c]
                  color=c
            jugador["mano"][idCartaSeleccionada]["color"]=c
         repetir=False
   cartaEscogida=jugador["mano"][idCartaSeleccionada]
   jugador["mano"]=jugador["mano"][0:int(idCartaSeleccionada)]+jugador["mano"][int(idCartaSeleccionada)+1:]
   return cartaEscogida,baraja

colores=["NEGRO", "AZUL", "VERDE", "ROJA", "AMARILLA"]
baraja=[] #La baraja de cartas sin cojer
monton=[] #El montón en la mesa

baraja=crearBaraja()

jugadores=[
   {"nombre":"","mano":[], "tipo":"HUMANO"},
   {"nombre":"robot1","mano":[], "tipo": "IA"},
   {"nombre":"robot2","mano":[], "tipo": "IA"},
   {"nombre":"robot3","mano":[], "tipo": "IA"}
]
jugadores[0]["nombre"]=input("Dime tu nombre:")

for _ in range(7):
   for jugador in jugadores:
      jugador["mano"].append(baraja[0])
      baraja=baraja[1:]

#print(baraja)
#print(len(baraja))

#for jugador in jugadores:
#   print(jugador["nombre"])
#   print ("MANO")
#   for carta in jugador["mano"]:
#      print(((carta["color"]+" ") if carta["color"]!="NEGRO" else "") +carta["valor"])

monton.append(baraja[0])
baraja=baraja[1:]
if(monton[0]["color"]=="NEGRO"):
   monton[0]["color"]=rd.choice(colores[1:])

#JUEGO
continuar=True
idJugador=0
direccionJuego=+1
numeroJugadores=len(jugadores)
while continuar:
   if len(baraja)<=0:
      continuar=False
   if monton[-1]["valor"]=="SALTO":
      idJugador+=direccionJuego   
      idJugador=(numeroJugadores+idJugador) if idJugador<0 else idJugador % numeroJugadores
   
   jugador=jugadores[idJugador]
   print("\r\nTurno de " + jugador["nombre"])
   baraja=controlaRobos(jugador,monton[-1],baraja)

   if jugador["tipo"]=="IA":
      cartaEscogida,baraja=jugarCarta(jugador,monton[-1],baraja)
      print(bcolors.BOLD+ "\tTira "+pintarCarta(cartaEscogida)+bcolors.ENDC)
   else:
      cartaEscogida,baraja=escogerCarta(jugador,monton[-1],baraja)
   if cartaEscogida!=None:
      cartaEscogida["robar"]+=monton[-1]["robar"]
      monton.append(cartaEscogida)
   if len(jugador["mano"])==0:
      continuar=False
      print (jugador["nombre"]+ "  GANA LA PARTIDA")
   if monton[-1]["valor"]=="CAMBIO":
      direccionJuego*=-1
   idJugador+=direccionJuego
   idJugador=(numeroJugadores+idJugador) if idJugador<0 else idJugador % numeroJugadores
   

