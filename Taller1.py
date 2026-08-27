import random
 
def ejecutar_programa():
    # 1. Definicion del alfabeto
    print("\n--- Definicion del alfabeto ---")
    entrada = input("Ingrese los simbolos del alfabeto separados por coma (ej: a,b): ")
    alfabeto = [s.strip() for s in entrada.split(",")]
    print("Alfabeto (Σ) =", alfabeto)
 
    # 2. Generacion de cadenas
    print("\n--- Generacion de cadenas ---")
    n = int(input("Cuantas cadenas quiere generar? "))
    longitud_max = int(input("Longitud maxima de las cadenas? "))
 
    for i in range(n):
        largo = random.randint(1, longitud_max)
        cadena = "".join(random.choice(alfabeto) for _ in range(largo))
        print("Cadena aleatoria:", cadena, "- Longitud:", len(cadena))
 
    # 3. Definicion de lenguaje
    print("\n--- Definicion del lenguaje ---")
    entrada = input("Ingrese las cadenas del lenguaje separadas por coma (ej: a,ab,bb,aba): ")
    lenguaje = [c.strip() for c in entrada.split(",")]
    print("L =", lenguaje)
 
    # 4. Verificacion de pertenencia
    print("\n--- Verificacion de pertenencia ---")
    cantidad = int(input("Cuantas cadenas quiere verificar? "))
    for i in range(cantidad):
        cadena = input("Ingrese una cadena a verificar: ")
        print(f"¿'{cadena}' pertenece al lenguaje? ->", cadena in lenguaje)
 
 
# Programa principal
while True:
    ejecutar_programa()
    opcion = input("\nDesea hacer otra prueba? (s/n): ")
    if opcion.lower() != "s":
        print("Fin del programa.")
        break
 

