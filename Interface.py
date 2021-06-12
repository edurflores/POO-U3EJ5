from zope.interface import Interface
from zope.interface import Implementer

class IPrueba(Interface):
    def insertarElemento(elemento,posicion):
        pass
    
    def agregarElemento(elemento):
        pass
    
    def mostrarElemento(posicion):
        pass