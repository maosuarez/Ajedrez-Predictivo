
class Pieza:
    lista_letras = list("abcdefgh")
    def __init__(self,color,posicion_x,posicion_y,casilla,tipo_color)  -> None:
        self.color=color
        self.posicion_x=posicion_x
        self.posicion_y=posicion_y
        self.casilla = casilla
        self.tipo_color = tipo_color
        self.historial_movimientos = [casilla]

    def modify_casilla(self,nueva_casilla, casillas)  -> None :
        self.casilla = nueva_casilla
        self.posicion_x, self.posicion_y = casillas[nueva_casilla]
        self.historial_movimientos.append(nueva_casilla)
    
    def get_casilla(self,casilla)  -> tuple:
        letra = list(casilla)[0]
        numero = int(casilla[1])
        valor = self.lista_letras.index(letra)
        return letra, numero, valor
    
    def casillas_ocupadas(self, lista_blancos, lista_negros)-> list:
        casillas_ocupadas_blancas=[]
        casillas_ocupadas_negras=[]
        for blanco in lista_blancos:
            casillas_ocupadas_blancas.append(blanco.casilla)
        for negro in lista_negros:
            casillas_ocupadas_negras.append(negro.casilla)
        casillas_no_disponibles = casillas_ocupadas_blancas + casillas_ocupadas_negras
        return casillas_ocupadas_blancas , casillas_ocupadas_negras, casillas_no_disponibles

class Pawn(Pieza):
    def __init__(self,color,posicion_x,posicion_y,casilla,tipo_color)  -> None:
        super().__init__(color,posicion_x,posicion_y,casilla,tipo_color)

    def __str__(self) -> str:
        return "peon"
    
    def movimiento_posibles(self, lista_notacion_blancos, lista_notacion_negros, lista_blancos,lista_negros):
        
        posibles_movimientos = []
        letra, num , valor = self.get_casilla(self.casilla)
        casillas_ocupadas_blancas , casillas_ocupadas_negras, casillas_no_disponibles = self.casillas_ocupadas(lista_blancos,lista_negros)
        
        if self.color == "blanco":
            num += 1
            if f"{self.lista_letras[valor]}{num}" not in casillas_no_disponibles:
                posibles_movimientos.append(f"{self.lista_letras[valor]}{num}")
                if num-1 == 2:
                    if f"{self.lista_letras[valor]}{num+1}" not in casillas_no_disponibles:
                        posibles_movimientos.append(f"{self.lista_letras[valor]}{num+1}")
            if valor-1 >= 0:
                if f"{self.lista_letras[valor-1]}{num}" in casillas_ocupadas_negras:
                   posibles_movimientos.append(f"{self.lista_letras[valor-1]}{num}")
            if valor+1 <= 7:
                if f"{self.lista_letras[valor+1]}{num}" in casillas_ocupadas_negras:
                   posibles_movimientos.append(f"{self.lista_letras[valor+1]}{num}")
            if self.casilla[1] == "5":
                if num-1 == 5 and len(lista_notacion_negros) != 0:
                    if valor +1 <= 7:
                        if (lista_notacion_negros[-1] == f"P{self.lista_letras[valor+1]}{num-1}\t") and (f"P{self.lista_letras[valor+1]}{num}\t" not in lista_notacion_negros):
                            posibles_movimientos.append(f"{self.lista_letras[valor+1]}{num}")
                    if  valor -1 >= 0 :
                        if (lista_notacion_negros[-1] == f"P{self.lista_letras[valor-1]}{num-1}\t") and (f"P{self.lista_letras[valor-1]}{num}\t" not in lista_notacion_negros):
                            posibles_movimientos.append(f"{self.lista_letras[valor-1]}{num}")
        if self.color == "negro":
            num -= 1
            if f"{self.lista_letras[valor]}{num}" not in casillas_no_disponibles:
                posibles_movimientos.append(f"{self.lista_letras[valor]}{num}")
                if num+1 == 7:
                    if f"{self.lista_letras[valor]}{num-1}" not in casillas_no_disponibles:
                        posibles_movimientos.append(f"{self.lista_letras[valor]}{num-1}")
            if valor-1 >= 0:
                if f"{self.lista_letras[valor-1]}{num}" in casillas_ocupadas_blancas or lista_notacion_blancos[-1]== f"{self.lista_letras[valor-1]}{num-1}":
                   posibles_movimientos.append(f"{self.lista_letras[valor-1]}{num}") 
            if valor+1 <= 7:
                if f"{self.lista_letras[valor+1]}{num}" in casillas_ocupadas_blancas or lista_notacion_blancos[-1]== f"{self.lista_letras[valor+1]}{num-1}":
                   posibles_movimientos.append(f"{self.lista_letras[valor+1]}{num}")
            if self.casilla[1] == "4":
                if num+1 == 4 and len(lista_notacion_blancos) != 0:
                    if valor +1 <= 7:
                        if lista_notacion_blancos[-1] == f"P{self.lista_letras[valor+1]}{num+1}\t" and f"P{self.lista_letras[valor+1]}{num}\t" not in lista_notacion_blancos:
                            posibles_movimientos.append(f"{self.lista_letras[valor+1]}{num}")
                    if  valor -1 >= 0 :
                        if lista_notacion_blancos[-1] == f"P{self.lista_letras[valor-1]}{num+1}\t" and f"P{self.lista_letras[valor-1]}{num}\t" not in lista_notacion_blancos:
                            posibles_movimientos.append(f"{self.lista_letras[valor-1]}{num}")
        
        return posibles_movimientos

class Bishop(Pieza):
    def __init__(self,color,posicion_x,posicion_y,casilla,tipo_color):
        super().__init__(color,posicion_x,posicion_y,casilla,tipo_color)

    def __str__(self) -> str:
        return "alfil"
    
    def movimiento_posibles(self, lista_notacion_blancos, lista_notacion_negros, lista_blancos,lista_negros):

        posibles_movimientos = []
        letra, numero , valor = self.get_casilla(self.casilla)
        casillas_ocupadas_blancas , casillas_ocupadas_negras, casillas_no_disponibles = self.casillas_ocupadas(lista_blancos,lista_negros)

        for i in [0,1,-1]:
            for j in [0,1,-1]:
                a = 0
                num=numero
                valor = self.lista_letras.index(letra)
                if abs(i)==abs(j):
                    while a != 1:
                        num= num+i
                        valor = valor +j
                        if num <= 8 and num >=1 and valor >= 0 and valor <= 7 :
                            if f"{self.lista_letras[valor]}{num}" not in casillas_no_disponibles:
                                posibles_movimientos.append(f"{self.lista_letras[valor]}{num}")
                            else:
                                if self.color == "blanco":
                                    if f"{self.lista_letras[valor]}{num}" in casillas_ocupadas_blancas:
                                        a=1
                                    elif f"{self.lista_letras[valor]}{num}" in casillas_ocupadas_negras:
                                        posibles_movimientos.append(f"{self.lista_letras[valor]}{num}")
                                        a=1
                                elif self.color == "negro":
                                    if f"{self.lista_letras[valor]}{num}" in casillas_ocupadas_negras:
                                        a=1
                                    elif f"{self.lista_letras[valor]}{num}" in casillas_ocupadas_blancas:
                                        posibles_movimientos.append(f"{self.lista_letras[valor]}{num}")
                                        a=1
                        else:
                            a=1
        return posibles_movimientos  

class Rook (Pieza):
    def __init__(self,color,posicion_x,posicion_y,casilla,tipo_color):
        super().__init__(color,posicion_x,posicion_y,casilla,tipo_color)

    def __str__(self) -> str:
        return "torre"
    
    def movimiento_posibles(self, lista_notacion_blancos, lista_notacion_negros, lista_blancos,lista_negros):

        posibles_movimientos = []
        letra, numero , valor = self.get_casilla(self.casilla)
        casillas_ocupadas_blancas , casillas_ocupadas_negras, casillas_no_disponibles = self.casillas_ocupadas(lista_blancos,lista_negros)

        for i in [0,1,-1]:
            for j in [0,1,-1]:
                a = 0
                num=numero
                valor = self.lista_letras.index(letra)
                if not abs(i)==abs(j):
                    while a != 1:
                        num= num+i
                        valor = valor +j
                        if num <= 8 and num >=1 and valor >= 0 and valor <= 7 :
                            if f"{self.lista_letras[valor]}{num}" not in casillas_no_disponibles:
                                posibles_movimientos.append(f"{self.lista_letras[valor]}{num}")
                            else:
                                if self.color == "blanco":
                                    if f"{self.lista_letras[valor]}{num}" in casillas_ocupadas_blancas:
                                        a=1
                                    elif f"{self.lista_letras[valor]}{num}" in casillas_ocupadas_negras:
                                        posibles_movimientos.append(f"{self.lista_letras[valor]}{num}")
                                        a=1
                                elif self.color == "negro":
                                    if f"{self.lista_letras[valor]}{num}" in casillas_ocupadas_negras:
                                        a=1
                                    elif f"{self.lista_letras[valor]}{num}" in casillas_ocupadas_blancas:
                                        posibles_movimientos.append(f"{self.lista_letras[valor]}{num}")
                                        a=1
                        else:
                            a=1
        
        return posibles_movimientos
    
class Knight(Pieza):
    def __init__(self,color,posicion_x,posicion_y,casilla,tipo_color):
        super().__init__(color,posicion_x,posicion_y,casilla,tipo_color)

    def __str__(self) -> str:
        return "caballo"
    
    def movimiento_posibles(self, lista_notacion_blancos, lista_notacion_negros, lista_blancos,lista_negros):
        
        posibles_movimientos = []
        letra, numero , valor = self.get_casilla(self.casilla)
        casillas_ocupadas_blancas , casillas_ocupadas_negras, casillas_no_disponibles = self.casillas_ocupadas(lista_blancos,lista_negros)
        
        for i in [1,-1,2,-2]:
            for j in [1,-1,2,-2]:
                num=numero
                valor = self.lista_letras.index(letra)
                comprobante=abs(i)+abs(j) 
                if comprobante==3:
                    valor = valor + i
                    num = num + j
                    if valor <=7 and valor >= 0 and num <= 8 and num >= 1:
                        if f"{self.lista_letras[valor]}{num}" not in casillas_no_disponibles:
                            posibles_movimientos.append(f"{self.lista_letras[valor]}{num}")
                        else:
                            if self.color == "blanco":
                                if f"{self.lista_letras[valor]}{num}" in casillas_ocupadas_blancas:
                                    pass
                                elif f"{self.lista_letras[valor]}{num}" in casillas_ocupadas_negras:
                                    posibles_movimientos.append(f"{self.lista_letras[valor]}{num}")
                            elif self.color == "negro":
                                if f"{self.lista_letras[valor]}{num}" in casillas_ocupadas_negras:
                                    pass
                                elif f"{self.lista_letras[valor]}{num}" in casillas_ocupadas_blancas:
                                        posibles_movimientos.append(f"{self.lista_letras[valor]}{num}")

        return posibles_movimientos      

class Dama(Pieza):
    def __init__(self,color,posicion_x,posicion_y,casilla,tipo_color):
        super().__init__(color,posicion_x,posicion_y,casilla,tipo_color)

    def __str__(self) -> str:
        return "dama"
    
    def movimiento_posibles(self, lista_notacion_blancos, lista_notacion_negros, lista_blancos,lista_negros):
        
        posibles_movimientos = []
        letra, numero , valor = self.get_casilla(self.casilla)
        casillas_ocupadas_blancas , casillas_ocupadas_negras, casillas_no_disponibles = self.casillas_ocupadas(lista_blancos,lista_negros)

        # Caracteristicas 
        for i in [0,1,-1]:
            for j in [0,1,-1]:
                a = 0
                num=numero
                valor = self.lista_letras.index(letra)
                while a != 1:
                    num= num+i
                    valor = valor +j
                    if num <= 8 and num >=1 and valor >= 0 and valor <= 7 :
                        if f"{self.lista_letras[valor]}{num}" not in casillas_no_disponibles:
                            posibles_movimientos.append(f"{self.lista_letras[valor]}{num}")
                        else:
                            if self.color == "blanco":
                                if f"{self.lista_letras[valor]}{num}" in casillas_ocupadas_blancas:
                                    a=1
                                elif f"{self.lista_letras[valor]}{num}" in casillas_ocupadas_negras:
                                    posibles_movimientos.append(f"{self.lista_letras[valor]}{num}")
                                    a=1
                            elif self.color == "negro":
                                if f"{self.lista_letras[valor]}{num}" in casillas_ocupadas_negras:
                                    a=1
                                elif f"{self.lista_letras[valor]}{num}" in casillas_ocupadas_blancas:
                                    posibles_movimientos.append(f"{self.lista_letras[valor]}{num}")
                                    a=1
                    else:
                        a=1
    
        return posibles_movimientos

class King(Pieza):
    def __init__(self,color,posicion_x,posicion_y,casilla,tipo_color):
        super().__init__(color,posicion_x,posicion_y,casilla,tipo_color)

    def __str__(self) -> str:
        return "rey"
    
    def enroque(self,posibles_movimientos,lista_blancos,lista_negros):
        
        letra, numero , valor = self.get_casilla(self.casilla)
        casillas_ocupadas_blancas , casillas_ocupadas_negras, casillas_no_disponibles = self.casillas_ocupadas(lista_blancos,lista_negros)

        if movimientos_rey_n:
            if movimientos_torre_a_n:
                if not "c8" in casillas_no_disponibles: 
                    if not "b8" in casillas_no_disponibles:
                        if not "d8" in casillas_no_disponibles:
                            a = 0
                            for x in lista_blancos:
                                for k in x[5].movimiento_posibles():
                                    if k == "c8":
                                        a = 1
                                    elif k == "d8":
                                        a = 1
                                    elif k == "e8":
                                        a = 1
                                    else:
                                        pass
                            if a == 0:
                                posibles_movimientos.append("c8")
                                enroque_negro = True
            if movimientos_torre_h_n:
                if not "f8" in casillas_no_disponibles:
                    if not "g8" in casillas_no_disponibles:
                        a = 0
                        for x in lista_blancos:
                            for k in x[5].movimiento_posibles():
                                if k == "f8":
                                    a = 1
                                elif k == "g8":
                                    a = 1
                                elif k=="e8":
                                    a = 1
                        if a == 0:
                            posibles_movimientos.append("g8")
                            enroque_negro = True
        if movimientos_rey_b:
            if movimientos_torre_a_b:
                if not "c1"  in casillas_no_disponibles: 
                    if not "b1"  in casillas_no_disponibles:
                        if not  "d1" in casillas_no_disponibles:
                            a = 0
                            for x in lista_negros:
                                for k in x[5].movimiento_posibles():
                                    if k == "c1":
                                        a = 1
                                    elif k == "b1":
                                        a = 1
                                    elif k=="d1":
                                        a = 1
                                    elif k == "e1":
                                        a =1
                            if a == 0:
                                posibles_movimientos.append("c1")
                                enroque_blanco = True
            if movimientos_torre_h_b:
                if 'f1' not in casillas_no_disponibles:
                    if not "g1" in casillas_no_disponibles:
                        a = 0
                        for x in lista_negros:
                            for k in x[5].movimiento_posibles():
                                if k == "f1":
                                    a = 1
                                elif k == "g1":
                                    a = 1
                                elif k=="e1":
                                    a = 1
                        if a == 0:
                            posibles_movimientos.append("g1")
                            enroque_blanco = True
        return posibles_movimientos

    def movimiento_posibles(self, lista_notacion_blancos, lista_notacion_negros, lista_blancos,lista_negros):
        
        posibles_movimientos = []
        letra, numero , valor = self.get_casilla(self.casilla)
        casillas_ocupadas_blancas , casillas_ocupadas_negras, casillas_no_disponibles = self.casillas_ocupadas(lista_blancos,lista_negros)

        for i in [0,1,-1]:
            for j in [0,1,-1]:
                valor = self.lista_letras.index(letra)
                num = numero
                num= num+i
                valor = valor +j
                if num <= 8 and num >=1 and valor >= 0 and valor <= 7 :
                                if f"{self.lista_letras[valor]}{num}" not in casillas_no_disponibles:
                                    posibles_movimientos.append(f"{self.lista_letras[valor]}{num}")
                                else:
                                    if self.color == "blanco":
                                        if f"{self.lista_letras[valor]}{num}" in casillas_ocupadas_negras:
                                            posibles_movimientos.append(f"{self.lista_letras[valor]}{num}")
                                    elif self.color == "negro":
                                        if f"{self.lista_letras[valor]}{num}" in casillas_ocupadas_blancas:
                                            posibles_movimientos.append(f"{self.lista_letras[valor]}{num}")
        return posibles_movimientos