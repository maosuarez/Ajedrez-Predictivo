import time
from Piezas import *

class Funciones:
    lista_letras = list("abcdefgh")

    @classmethod
    def casillas(cls) -> dict:
        lista_casillas = {}
        var_x = 0
        for letra in cls.lista_letras:
            for numero in range(1,9):
                casilla = f"{letra}{numero}"
                x = float(75 * var_x)
                y = float(75 * (8-numero))
                valor_x_y = (x,y)
                lista_casillas[casilla]=valor_x_y
            var_x +=1
        return lista_casillas
    
    @staticmethod
    def mostrar_pieza(lista_objetos, pantalla):
        for pieza in lista_objetos.get_lista_blancos():
            pantalla.blit(pieza.imagen,(pieza.posx,pieza.posy))
        for pieza in lista_objetos.get_lista_negros():
            pantalla.blit(pieza.imagen,(pieza.posx,pieza.posy))

    @staticmethod
    def buscar_valor(lista,var):
        for key in lista.keys():
            if lista[key] == var:
                return key
        
    @staticmethod
    def objetivos():
        pass

    @staticmethod
    def LogIn():
        print("Hola, este es un juego de ajedrez predictivo.\n Extisten dos modos de juego.")
        print("\t1.- Piezas Predeterminadas")
        print("\t2.- Elegir mis propias piezas")
        while True:
            opcion=input("Elija una opción:\n")
            if opcion=="1":
                print("Muy bien el juego va a iniciar en corto")
                print("Cargando...")
                time.sleep(2)
                return False
            elif opcion=="2":
                return True
            else:
                print("Opción incorrecta.")

    @staticmethod
    def ElegirPiezas():
        def verificar(cantidad):
            lista = []
            i = 0
            diferente_peon = 0
            while i < cantidad:
                i+=1
                try:
                    if  diferente_peon<8:
                        opcion = int (input(f"Pieza #{i}  "))
                    elif  diferente_peon == 8:
                        print("El resto de piezas deben ser peones, para completar la segunda fila\n")
                        opcion = 1
                        diferente_peon += 1
                    else:
                        opcion = 1
                    if 1 <= opcion <= 6:
                        if 1 < opcion < 5 and lista.count(piezas[opcion - 1])<2:
                            lista.append(piezas[int(opcion)-1])
                            diferente_peon += 1
                        elif opcion > 4 and lista.count(piezas[opcion - 1])== 0:
                            lista.append(piezas[opcion - 1])
                            diferente_peon += 1
                        elif  opcion == 1 and lista.count(piezas[opcion - 1])<9:
                            lista.append(piezas[opcion - 1])
                        else:
                            print("Ya no puedes elegir mas esta pieza")
                            i -=1
                            continue
                    else:
                        i-=1
                except: i-= 1
            return  lista

        print("Muy bien, vamos a elegir las piezas con las que quieres jugar")
        while True:
            try:
                cantidad = int(input("Cuantas piezas por cada bando?  "))
                if 0<cantidad<=16:
                    break
            except:
                print("No has introducido un número correcto")
                continue
        print("Las opciones son:")
        print("1-Peon")
        print("2-Alfil")
        print("3-Caballo")
        print("4-Torre")
        print("5-Rey")
        print("6-Dama")
        print("(Digita solo el número)")
        piezas = ["peon","alfil","caballo","torre","rey","dama"]
        print("Elige las piezas para el bando blanco")
        blancas = verificar(cantidad)
        print("Elige las piezas para el bando negro")
        negras = verificar(cantidad)
        return blancas , negras
    
    @staticmethod
    def mostrar_piezas(blancas, negras):
        print("Las piezas que selecionadas son:")
        print("Las piezas blancas:")
        for i in range(len(blancas)):
            print(f"#{i+1} {blancas[i]}")
        print("Las piezas negras:")
        for i in range(len(negras)):
            print(f"#{i+1} {negras[i]}")

    @staticmethod
    def elegir_casillas(blancas, negras):
        def texto(opciones):
            texto1 = "("
            for c in opciones:
                texto1 += c + ","
            texto1 += ")"
            return  texto1 

        def aux_elegircasilla(pieza, fila, columnas, casillas):
            while True:
                letra = input(f"\nElige la casilla del {pieza}\n{texto(columnas)}\n").lower()
                casilla = f"{letra}{fila}"
                if letra in columnas and casilla not in casillas:
                    return casilla
                elif casilla in casillas:
                    print("\nEsa casilla ya tiene una pieza\n")
                else:
                    print( "No es una casilla valida")
        casillas_blancas = []
        casillas_negras = []
        lista_letras_alfil = ["c","f"]
        lista_letras_torre = ["a","h"]
        lista_letras_caballo = ["b","g"]
        lista_letras_peon = ['a','b','c','d','e','f','g','h']
        print("\nPara poder iniciar el juego se necesitan saber las casillas de inicio de las piezas seleccionadas.")
        i = 0
        while i < len(blancas):
            match  blancas[i]:
                case 'peon':
                    casillas_blancas.append(aux_elegircasilla(blancas[i],"2",lista_letras_peon,casillas_blancas))
                case "alfil" :
                    casillas_blancas.append(aux_elegircasilla(blancas[i],"1",lista_letras_alfil,casillas_blancas))
                case "caballo" :
                    casillas_blancas.append(aux_elegircasilla(blancas[i],"1",lista_letras_caballo,casillas_blancas))
                case "torre":
                    casillas_blancas.append(aux_elegircasilla(blancas[i],"1",lista_letras_torre,casillas_blancas))
                case "dama" :
                    casillas_blancas.append("d1")
                case "rey":
                    casillas_blancas.append("e1")
            match negras[i]:
                case 'peon' :
                    casillas_negras.append(aux_elegircasilla(negras[i],"7",lista_letras_peon,casillas_negras))
                case "alfil":
                    casillas_negras.append(aux_elegircasilla(negras[i],"8",lista_letras_alfil,casillas_negras))
                case "caballo":
                    casillas_negras.append(aux_elegircasilla(negras[i],"8",lista_letras_caballo,casillas_negras))
                case "torre":
                    casillas_negras.append(aux_elegircasilla(negras[i],"8",lista_letras_torre,casillas_negras))
                case "dama":
                    casillas_negras.append("d8")
                case "rey":
                    casillas_negras.append("e8")
            i += 1
        return  casillas_blancas,casillas_negras
    
    @staticmethod
    def mostrar_objetivos(pantalla, lista_objetivos, objetivo):
        for cosas in lista_objetivos:
            pantalla.blit(objetivo,cosas)

class Objetos:
    def __init__(self,casilla,color,posx, posy, imagen,pieza,descripcion) -> None:
        self.casilla = casilla
        self.color = color
        self.posx = posx
        self.posy = posy
        self.imagen = imagen
        self.pieza = pieza
        self.descripcion = descripcion

    def modify_casilla(self, casilla, casillas):
        self.pieza.modify_casilla(casilla, casillas)
        self.casilla = casilla
        self.posx = self.pieza.posicion_x
        self.posy = self.pieza.posicion_y

class Lista_Objetos:
    def __init__(self ) -> None:
        self.lista_blancos = []
        self.lista_negros = []

    def agregar_lista_blancos(self,pieza):
        self.lista_blancos.append(pieza)
    
    def agregar_lista_negros(self,pieza):
        self.lista_negros.append(pieza)

    def eliminar_pieza(self,color, indice):
        if color == "blanco":
            self.lista_blancos.pop(indice)
        elif color == "negro":
            self.lista_negros.pop(indice)    
        
    def get_lista_blancos(self):
        return self.lista_blancos
    
    def get_lista_negros(self):
        return self.lista_negros
    
    def identificar_pieza(self,casilla):
        for piezas in self.lista_blancos:
            if piezas.casilla == casilla:
                return piezas.pieza
        for  piezas in self.lista_negros:
            if piezas.casilla == casilla:
                return piezas.pieza
    
    def modificar_pieza(self,color, indice, i_torre, c_casilla, i_captura, casilla, casillas):
        if color == "blanco":
            objeto = self.lista_blancos.pop(indice)
            objeto.modify_casilla(casilla, casillas)
            self.agregar_lista_blancos(objeto)
            if  i_torre != "undefined":
                objeto = self.lista_blancos.pop(int(i_torre))
                objeto.modify_casilla(c_casilla, casillas)
                self.agregar_lista_blancos(objeto)
            elif  i_captura != "undefined":
                self.eliminar_pieza("negro", int(i_captura))
        elif color == "negro":
            objeto = self.lista_negros.pop(indice)
            objeto.modify_casilla(casilla, casillas)
            self.agregar_lista_negros(objeto)
            if  i_torre != "undefined":
                objeto = self.lista_negros.pop(int(i_torre))
                objeto.modify_casilla(c_casilla, casillas)
                self.agregar_lista_blancos(objeto)
            elif  i_captura != "undefined":
                self.eliminar_pieza("blanco", int(i_captura))

    def verificar_vacios(self, lista_ocupadas):
        for cosas in lista_ocupadas:
            pass

class Notacion():
    def __init__(self) -> None:
        self.lista_notacion_blancos = []
        self.lista_notacion_negros = []

    def  agregar_movimiento(self, movimiento, color):
        if color == "blanco":
            self.lista_notacion_blancos.append(movimiento)
        else:
            self.lista_notacion_negros.append(movimiento)

    def devolver_indice(self, color, indice):
        if color == "blanco":
            return self.lista_notacion_blancos[indice]
        else:
            return self.lista_notacion_negros[indice]
        
    def devolver_len(self,color):
        if color == "blanco":
            return len(self.lista_notacion_blancos)
        else:
            return len(self.lista_notacion_negros)
        
    def devolver(self, color):
        if color == "blanco":
            return self.lista_notacion_blancos
        else:
            return self.lista_notacion_negros