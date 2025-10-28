from contenedor import codigo
import random

class Bodega:
    def __init__(self):
        self.inventario = []
    def agregarContenedor(self, codigo, filas, columnas):       
        datos_contenedor = {
            "codigo": codigo,
            "filas": filas,
            "columnas": columnas
        }
        self.inventario.append(datos_contenedor)
        print(f"Contenedor '{codigo}' agregado.")
    def retirarContenedor(self, codigo, filas, columnas):
        for contenedor in self.inventario:
            if contenedor["codigo"] == codigo:
                self.inventario.remove(contenedor)
                print(f"Contenedor '{codigo}' retirado.")
                return
        print(f"Contenedor '{codigo}' no encontrado.")
    def buscarContenedor(self, codigo):
        for contenedor in self.inventario:
            if contenedor["codigo"] == codigo:
                print(f"Contenedor '{codigo}' encontrado.")
                return contenedor
        print(f"Contenedor '{codigo}' no encontrado.")
        return None
    def mostrarEstadoContenedor(self, codigo):
        contenedor = self.buscarContenedor(codigo)
        if contenedor:
            print(f"Estado del contenedor '{codigo}': Filas: {contenedor['filas']}, Columnas: {contenedor['columnas']}")

def generar_codigo():
    for i in range(504):
        nuevo_codigo = random.randint(1,504)
        nuevo_codigo = str(nuevo_codigo).zfill(4)

bodega = Bodega()
    
bodega.agregarContenedor(codigo, 0, 0) 

print("\n--- RESULTADOS ---")
print(f"Último código generado: {codigo}") 
print(f"Total de contenedores en inventario: {len(bodega.inventario)}")