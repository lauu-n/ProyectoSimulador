class Contenedor:
    def __init__(self, codigo):
        self.codigo = codigo

num_contenedores = 504
for i in range (num_contenedores):
    codigo = str(i+1).zfill(4)