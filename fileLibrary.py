DEBUG = False

class Baliza:
   def __init__(self, nombre, mac, posX, posY):
      self.nombre = nombre
      self.mac    = mac
      self.posX   = posX
      self.posY   = posY
"""
   def __str__(self):
      return self.nombre

   def getNombre(self):
      return self.nombre

   def getMac(self):
      return self.mac

   def getPosX(self):
      return self.posX

   def getPosY(self):
      return self.posY


def printList(lista):
   for baliza in lista:
      print baliza
"""
def readFile(name):
   f = open(name, "r")
   linea = f.readline()
   numLinea = 0
   friendList = []
   while linea != "":
#      values = linea.split("@")
#      nombre = values(1)
#      mac = values(2)
#      posX = values(3)
#      posY = values(4)
      nombre,mac,posX,posY= linea.split("@")
      baliza = Baliza(nombre, mac, posX, posY)
      friendList+= [baliza]
      numLinea=numLinea+1
      linea = f.readline()

   f.close()
   return friendList
"""
def obtenerMacs(lista):
   result = []
   for l in lista:
      result += [l.getMac]
   return result
"""
