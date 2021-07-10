class Colores:
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   END = '\033[0m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   RED   = "\033[1;31m"  
   BLUE  = "\033[1;34m"
   CYAN  = "\033[1;36m"
   GREEN = "\033[0;32m"
   REVERSE = "\033[;7m"
class Utilidades:
   @staticmethod
   def preguntarOpciones(texto,opciones):
      valor=""
      while not valor in opciones:
         valor=input(texto)
      return valor
   @staticmethod
   def preguntarNumero(texto,minimo, maximo):
      valor=minimo-1
      while valor<minimo or valor>maximo:
         valor=int(input(texto))
      return valor