import random
LLista_de_Coses = ["Random1","Random2","Random3","Random4"]
Juegos_Favoritos = ("Overwatch","Rust","CSGO","Legue of Legends")
Dades_Personals = {
    "Nombre" : "Unai",
    "Apellido" : "Anfruns",
    "Edat" : 18,
    "Esport Favorit" : "Escalada",
    "Enemic Mortal" : "Despertadors"
}
Personage_Favorito = {"Katarina","Tira una daga {Q}","Tira una daga en sus pies {W}","Se teleporta a una daga {E}","Gira Mucho {R}"}
def Mostrar_Lista():
    print(LLista_de_Coses)

def Mostar_Tupla():
    print(Juegos_Favoritos)

def Mostrar_Dades_Personals():
    print(Dades_Personals)

def Mostrar_Personage():
    print(Personage_Favorito)

def Retornar_Numero():
    num = int(input("Introduce un numero porfavor : "))
    while 1 <= num:
        num -= 1
        print(num)
def Bomba():
    numero_random = random.randint(1,5)
    while True:
        usr_ipt = int(input("Introduce un numero del 1 al 5 :  "))
        if usr_ipt == numero_random:
            print("Ha explotado la boma")
            break
        else:
            print("Vuelve a insertar un numero")

def Lista_de_Productos():
    x = 0
    producto = ["Pan","Tomate","Agua","Aceite"]
    precio_producto = ["1.5","2.25","3.25","15.15"]

    while True:
        try:
            if float(precio_producto[x]) >= 3:
                Considerado = "Caro"
            else:
                Considerado = "Barato"
            print("El producto {} tiene un precio de {} $ y es considerado {}".format(producto[x],str(precio_producto[x]),Considerado))
            x += 1
        except:
            break
def Nom_de_personas():
    personas = ["Tom","Alfredo","Pau","Nuria","Oscar","Laura","Unai"]
    for personas_letras in personas:
        print("El nombre {} tiene un total de {} letras".format(personas_letras,len(personas_letras)))
if __name__ == '__main__':
    Mostrar_Lista()
    Mostar_Tupla()
    Mostrar_Dades_Personals()
    Mostrar_Personage()
    Retornar_Numero()
    Bomba()
    Lista_de_Productos()
    Nom_de_personas()
