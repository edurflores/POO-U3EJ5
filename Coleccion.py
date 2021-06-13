from zope.interface import Interface
from zope.interface import implementer
from Interface import IPrueba

@Implementer(IPrueba)

class ManejadorColeccion:
    __lista = []
    def __init__(self):
        self.__lista = []
    
    def insertarElemento(self,elemento,posicion):
        assert type(posicion) is int, "La posicion debe ser un numero entero"
        assert posicion > 0, "La posicion debe ser mayor a cero (numero positivo)"
        # Porque ya se resta dentro de la funcion una posicion para considerar la posicion 0.
        try:
            self.__lista[posicion - 1] = elemento
        except:
            print('Error. La posicion no es valida y no pudo insertarse el elemento.')
            
    def agregarElemento(self,elemento):
        self.__lista.append(elemento)
        
    def mostrarElemento(self,posicion):
        assert type(posicion) is int, "La posicion debe ser un numero entero"
        assert posicion > 0, "La posicion debe ser ser mayor a cero (numero positivo)"
        try:
            print('Elemento:',self.__lista[posicion -1 ])
        except:
            print('Error. La posicion no es valida y no puede mostrarse el elemento.')
