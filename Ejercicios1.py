class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print("Estudiando")

nombre = input("Ingresa tu nombre")
edad = input("Ingrese la edad")
grado = input("Ingrese el grado")

estudiante = Estudiante(nombre,edad,grado)

print(f"""Datos del estudiante: \n
      Nombre: {estudiante.nombre} \n
        edad: {estudiante.edad} \n
        Grado: {estudiante.grado} \n
    """)

estudiar = input()
if (estudiar.lower() == "estudiar"):
    estudiante.estudiar()