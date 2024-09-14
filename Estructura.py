#Importaciones
import pygame
from Piezas import *
from Funciones import *
from Prediccion import *
import copy


#Clases Locales

class PyJuego:
    def __init__(self) -> None:
        pygame.init()
        self.pantalla = pygame.display.set_mode((600, 600))
        self.cargar_imagenes()
        self.set_variables()
        self.set_display()
        self.variables_semiGlobales()
        
    def set_variables(self)  -> None:
        self.convertirse = True
        self.lista_letras = list("abcdefgh")
        self.lista_objetos = Lista_Objetos()
        self.lista_casillas = Funciones.casillas()
        self.notacion = Notacion()
        self.lista_objetivos = []

    def set_display(self)  -> None:
        pygame.display.set_caption("Ajedrez Mao")
        pygame.display.set_icon(self.icono)

    def  cargar_imagenes(self)  -> None:
        self.icono = pygame.image.load("Imagenes\\Pawn Blanco.png")
        self.fondo = pygame.image.load("Imagenes\\tablero_ajedrez.jpg")
        self.fondo_borroso = pygame.image.load("Imagenes\\borroso.jpg") 
        self.img_pawn_blanco = pygame.image.load("Imagenes\\Pawn Negro.png")
        self.img_pawn_negro = pygame.image.load("Imagenes\\Pawn Blanco.png")
        self.img_bishop_negro = pygame.image.load("Imagenes\\Bishop Negro.png")
        self.img_bishop_blanco = pygame.image.load("Imagenes\\Bishop Blanco.png")
        self.img_knight_negro = pygame.image.load("Imagenes\\Knight Negro.png")
        self.img_knight_blanco = pygame.image.load("Imagenes\\Knigth Blanco.png")
        self.img_rook_negro = pygame.image.load("Imagenes\\Rook Negra.png")
        self.img_rook_blanco = pygame.image.load("Imagenes\\Rook Blanca.png")
        self.img_dama_negro = pygame.image.load("Imagenes\\Dama Negra.png")
        self.img_dama_blanco = pygame.image.load("Imagenes\\Dama Blanca.png")
        self.img_king_negro = pygame.image.load("Imagenes\\King Negro.png")
        self.img_king_blanco = pygame.image.load("Imagenes\\King Blanco.png")
        self.objetivo = pygame.image.load("Imagenes\\punto.png")
    
    #Metodos get
    def get_pawn_blanco(self)  -> pygame.Surface: 
        return self.img_pawn_blanco
    def get_pawn_negro(self)   -> pygame.Surface: 
        return self.img_pawn_negro
    def get_alfil_blanco(self) -> pygame.Surface :
        return self.img_bishop_blanco
    def get_alfil_negro(self) -> pygame.Surface:
        return self.img_bishop_negro
    def get_caballo_blanco(self) -> pygame.Surface:
        return self.img_knight_blanco
    def get_caballo_negro(self) -> pygame.Surface:
        return self.img_knight_negro
    def get_torre_blanco(self) -> pygame.Surface:
        return self.img_rook_blanco
    def get_torre_negro(self) -> pygame.Surface:
        return self.img_rook_negro
    def get_dama_blanco(self) -> pygame.Surface:
        return self.img_dama_blanco
    def get_dama_negro(self) -> pygame.Surface:
        return self.img_dama_negro
    def get_rey_blanco(self) -> pygame.Surface:
        return self.img_king_blanco
    def get_rey_negro(self) -> pygame.Surface:
        return self.img_king_negro
    def get_objetivo(self) -> pygame.Surface:
        return self.objetivo

    def accion_promover(self):
        var = pygame.mouse.get_pos()
        cor_x , cor_y = self.lista_casillas[self.llegada_coronacion]
        casilla = self.llegada_coronacion

        self.lista_objetos.eliminar_pieza(self.color_reemplazar,self.indice_coronacion)

        print(f"P={self.escribir_notacion(self.llegada_coronacion,self.clase_pieza.casilla,self.clase_pieza)}")
    
        if var[1]<=124:
            if self.color_reemplazar == "negro":
                ficha = Dama("negro",cor_x,cor_y,casilla,"dama_negro")
                imagen = self.get_dama_negro()
            if self.color_reemplazar == "blanco":
                ficha = Dama("blanco",cor_x,cor_y,casilla,"dama_blanco")
                imagen = self.get_dama_blanco()
        elif var[1]<=218:
            if self.color_reemplazar == "negro":
                ficha = Bishop("negro",cor_x,cor_y,casilla,"alfil_negro")
                imagen = self.get_alfil_negro()
            if self.color_reemplazar == "blanco":
                ficha = Bishop("blanco",cor_x,cor_y,casilla,"alfil_blanco")
                imagen = self.get_alfil_blanco()
        elif var[1]<=312:
            if self.color_reemplazar == "negro":
                ficha = Knight("negro",cor_x,cor_y,casilla,"caballo_negro")
                imagen = self.get_caballo_negro()
            if self.color_reemplazar == "blanco":
                ficha = Knight("blanco",cor_x,cor_y,casilla,"caballo_blanco")
                imagen = self.get_caballo_blanco()
        elif var[1]<=400:
            if self.color_reemplazar == "negro":
                ficha = Rook("negro",cor_x,cor_y,casilla,"torre_negro")
                imagen = self.get_torre_negro()
            if self.color_reemplazar == "blanco":
                ficha = Rook("blanco",cor_x,cor_y,casilla,"torre_blanco")
                imagen = self.get_torre_blanco()
            

        objeto = Objetos(ficha.casilla,ficha.color,ficha.posicion_x,ficha.posicion_y,imagen,ficha,ficha.tipo_color)
        if self.color_reemplazar == "blanco":
            self.lista_objetos.agregar_lista_blancos(objeto)
        elif self.color_reemplazar == "negro":
            self.lista_objetos.agregar_lista_negros(objeto)
        self.convertirse = True

    def promocion(self)  -> None:
        self.pantalla.blit(self.fondo_borroso,(0,0))
        self.pantalla.blit(self.get_dama_blanco(),(268,30))
        self.pantalla.blit(self.get_alfil_blanco(),(268,128))
        self.pantalla.blit(self.get_caballo_blanco(),(268,218))
        self.pantalla.blit(self.get_torre_blanco(),(268,312))

    def piezas_iniciales(self, blancas, negras, casillas_blancas, casillas_negras)  -> None:
        def aux(pieza, color, casilla) -> Objetos:
            texto_tipo = f"{pieza}_{color}" 
            match pieza:
                case 'peon' :
                    ficha = Pawn(color,self.lista_casillas[casilla][0]+5.5,self.lista_casillas[casilla][1]+5.5,casilla,texto_tipo)
                    imagen = self.get_pawn_blanco() if color == "blanco" else self.get_pawn_negro()
                    objeto = Objetos(casilla,ficha.color,ficha.posicion_x,ficha.posicion_y,imagen,ficha,texto_tipo)
                case "alfil":
                    ficha = Bishop(color,self.lista_casillas[casilla][0]+5.5,self.lista_casillas[casilla][1]+5.5,casilla,texto_tipo)
                    imagen = self.get_alfil_blanco() if color == "blanco" else self.get_alfil_negro()
                    objeto = Objetos(casilla,ficha.color,ficha.posicion_x,ficha.posicion_y,imagen,ficha,texto_tipo)
                case "caballo":
                    ficha = Knight(color,self.lista_casillas[casilla][0]+5.5,self.lista_casillas[casilla][1]+5.5,casilla,texto_tipo)
                    imagen = self.get_caballo_blanco() if color == "blanco" else self.get_caballo_negro()
                    objeto = Objetos(casilla,ficha.color,ficha.posicion_x,ficha.posicion_y,imagen,ficha,texto_tipo)
                case "torre":
                    ficha = Rook(color,self.lista_casillas[casilla][0]+5.5,self.lista_casillas[casilla][1]+5.5,casilla,texto_tipo)
                    imagen = self.get_torre_blanco() if color == "blanco" else self.get_torre_negro()
                    objeto = Objetos(casilla,ficha.color,ficha.posicion_x,ficha.posicion_y,imagen,ficha,texto_tipo)
                case "dama":
                    ficha = Dama(color,self.lista_casillas[casilla][0]+5.5,self.lista_casillas[casilla][1]+5.5,casilla,texto_tipo)
                    imagen = self.get_dama_blanco() if color == "blanco" else self.get_dama_negro()
                    objeto = Objetos(casilla,ficha.color,ficha.posicion_x,ficha.posicion_y,imagen,ficha,texto_tipo)
                case "rey":
                    texto_tipo = f"king_{color}"
                    ficha = King(color,self.lista_casillas[casilla][0]+5.5,self.lista_casillas[casilla][1]+5.5,casilla,texto_tipo)
                    imagen = self.get_rey_blanco() if color == "blanco" else self.get_rey_negro()
                    objeto = Objetos(casilla,ficha.color,ficha.posicion_x,ficha.posicion_y,imagen,ficha,texto_tipo)
            return objeto
        for i in range(len(blancas)):
            self.lista_objetos.agregar_lista_blancos(aux(blancas[i],"blanco", casillas_blancas[i]))
            self.lista_objetos.agregar_lista_negros(aux(negras[i],"negro", casillas_negras[i]))

    def variables_semiGlobales(self) -> None:
        self.objeto = False
        self.confirmar1 = False
        self.se_captura_pieza = False
        self.romper = False

        self.enroque_negro = True
        self.enroque_blanco = True
        self.movimientos_torre_h_n = True
        self.movimientos_torre_a_n = True
        self.movimientos_torre_h_b = False
        self.movimientos_torre_a_b = False

        self.color_reemplazar = ""
        self.inicio = ""
        self.fin = ""

        self.ennrrooqquuee = 0

    def acciones_principales(self) -> None:
        var = pygame.mouse.get_pos()
        x = var[0]%75
        y = var[1]%75
        coordenada_casilla = (var[0]-x,var[1]-y)
        casilla_seleccionada=Funciones.buscar_valor(self.lista_casillas,coordenada_casilla)
        self.objeto = False
        try:
            if self.clase_pieza.color == "blanco" and (self.notacion.devolver_len("blanco")==self.notacion.devolver_len("negro")):
                indice, i_torre , i_captura, c_torre = self.se_juega(self.posibles,casilla_seleccionada,self.clase_pieza,self.salida)
            elif self.clase_pieza.color == "negro" and (self.notacion.devolver_len("blanco")==self.notacion.devolver_len("negro")+1):
                indice, i_torre , i_captura, c_torre = self.se_juega(self.posibles,casilla_seleccionada,self.clase_pieza,self.salida)
        except  Exception as e:
            print("mal en acciones principales ",e)
        if self.romper:
            self.convertirse = False
            return 
        else:
            print(self.objeto)
            if self.objeto:
                self.lista_objetos.modificar_pieza(self.clase_pieza.color, indice, i_torre, c_torre, i_captura, casilla_seleccionada, self.lista_casillas)
                print(self.lista_objetos.get_lista_blancos()[0].casilla)
                print(self.escribir_notacion(casilla_seleccionada,self.salida, self.clase_pieza))
            else:
                try:
                    lista_blancos = self.lista_objetos.get_lista_blancos()
                    lista_negros = self.lista_objetos.get_lista_negros()
                    self.clase_pieza = self.lista_objetos.identificar_pieza(casilla_seleccionada)
                    self.posibles = self.clase_pieza.movimiento_posibles(self.notacion.lista_notacion_blancos, self.notacion.lista_notacion_negros, lista_blancos,lista_negros)
                except:
                    pass
                finally:
                    self.salida = casilla_seleccionada
                    self.confirmar1 = True
        return
    
    def se_juega(self,posibles,llegada,clase_pieza,salida) -> tuple:#Confirmar1 == var4 #Clase_pieza = elemento Pieza
        lista_blancos = self.lista_objetos.get_lista_blancos()
        lista_negros = self.lista_objetos.get_lista_negros()
        tupla = (clase_pieza, salida, llegada)
        self.se_captura_pieza = False
        if self.confirmar1:
            casillas_ocupadas_blancas,casillas_ocupadas_negras,casillas_no_disponibles = clase_pieza.casillas_ocupadas(lista_blancos,lista_negros)
            if llegada in posibles:
                if clase_pieza.color == "blanco":
                    indice, i_torre, i_captura, c_torre = self.acciones_especiales(tupla,lista_blancos, lista_negros,5,1,casillas_ocupadas_negras)
                elif clase_pieza.color == "negro":
                    indice, i_torre, i_captura, c_torre = self.acciones_especiales(tupla,lista_negros,lista_blancos,4,8,casillas_ocupadas_blancas)
                self.objeto = True
            self.confirmar1 = False
            return indice, i_torre, i_captura,c_torre
        return 0,0,0,0
    
    def acciones_especiales(self, tupla, lista, otra_lista, fila_ideal, fila , casillas_ocupadas_color) -> tuple:
        def devolver_enroque(clase_pieza):
            if clase_pieza.color == "blanco":
                return self.enroque_blanco 
            elif clase_pieza.color == "negro":
                self.enroque_negro
        def devolver_variable(lado, color):
            if color == "blanco":
                if lado == "a":
                    
                    return self.movimientos_torre_a_b

            elif color == "negro":
                pass        
        def modificar_variables(clase_pieza, pieza):
            if clase_pieza.color == "blanco":
                if  pieza == "rey":
                    self.enroque_blanco = False
                if pieza == "torre":
                    if  clase_pieza.casilla[0] == "a":
                        self.movimientos_torre_a_b = False
                    elif clase_pieza.casilla[0] == "h":
                        self.movimientos_torre_h_b = False
                
            elif clase_pieza.color == "negro":
                if  pieza == "rey":
                    self.enroque_negro = False
                if pieza == "torre":
                    if  clase_pieza.casilla[0] == "a":
                        self.movimientos_torre_a_n = False
                    elif clase_pieza.casilla[0] == "h":
                        self.movimientos_torre_h_n = False

        clase_pieza, salida, llegada = tupla
        opc1, opc2 = (f"c{fila}",f"g{fila}")
        indice_torre_enroque = "undefined"
        indice_captura = "undefined"
        c_torre = "undefined"
        var6 = 0
        for pieza in lista:
            if pieza.casilla == salida :
                if clase_pieza.__str__() == "peon":
                    ideal = list(salida)
                    keep = int(ideal[1]) 
                    if keep == fila_ideal:
                        ideal= f"{ideal[0]}{fila_ideal}"
                        if llegada not in casillas_ocupadas_color:
                            aver = list(llegada)
                            aver[1] = str(keep)
                            llegada = "".join(aver)
                            cont = 0
                            for pieza in otra_lista:
                                if  pieza.casilla == f"{llegada[0]}{fila_ideal}":
                                    indice_captura = cont
                                    self.se_captura_pieza = True
                                    break
                                cont += 1
                    coronacion = list(llegada)
                    if int(coronacion[1]) == 8 or int(coronacion[1]) == 1:
                        self.indice_coronacion = 0
                        self.llegada_coronacion = llegada
                        for pieza in lista:
                            if pieza.casilla == salida:
                                break
                            self.indice_coronacion += 1
                        self.convertirse = False
                        self.color_reemplazar = clase_pieza.color
                        self.romper = True
                if pieza.__str__()== "rey":
                    if devolver_enroque(clase_pieza, pieza.__str__() ):
                        if llegada == opc1: #Enroque a C
                            c_torre = f"d{fila}"
                            self.eennrrooqquuee = 2
                            var_cuenta =0
                            for cosas in lista:
                                if cosas.casilla == "a1":
                                    indice_torre_enroque = var_cuenta
                                    break
                                var_cuenta += 1
                        if llegada == opc2: #Enroque en g
                            c_torre = f"f{fila}"
                            self.eennrrooqquuee = 1
                            var_cuenta = 0
                            for cosas in lista:
                                if cosas.casilla=="h1":
                                    indice_torre_enroque = var_cuenta
                                    break
                                var_cuenta+=1
                    modificar_variables(clase_pieza,pieza.__str__())
                if pieza.__str__() == "torre":
                    modificar_variables(clase_pieza,pieza.__str__())
                indice_pieza_seleccionada = var6
            else:
                var6 += 1

            if llegada in casillas_ocupadas_color:
                var6 = 0
                for pieza in lista:
                    if pieza.casilla == salida:
                        indice_pieza_seleccionada = var6
                    var6 += 1
                var6=0
                for pieza in otra_lista:
                    if pieza.casilla == llegada:
                        indice_captura = var6
                        self.se_captura_pieza = True
                        break
                    var6 += 1 
        return indice_pieza_seleccionada, indice_torre_enroque , indice_captura, c_torre

    def escribir_notacion(self, llegada, salida, pieza)  -> str:
        string = ""
        if pieza.color == "blanco":
            if self.convertirse:
                if self.se_captura_pieza:
                    self.notacion.agregar_movimiento(f"{pieza.tipo_color[0].upper()}{salida} x {llegada}", pieza.color)
                else:
                    if self.ennrrooqquuee == 0:
                        self.notacion.agregar_movimiento(f"{pieza.tipo_color[0].upper()}{llegada}\t", pieza.color)
                    elif self.ennrrooqquuee == 1:
                        self.notacion.agregar_movimiento(f"o-o\t",pieza.color)
                        self.ennrrooqquuee = 0
                    elif self.ennrrooqquuee == 2:
                        self.notacion.agregar_movimiento(f"o-o-o\t",pieza.color)
                        self.ennrrooqquuee = 0
            else:
                self.notacion.agregar_movimiento(f"P={pieza.tipo_color[0].upper()}{llegada}\t", pieza.color)
            for x in range(self.notacion.devolver_len(pieza.color)):
                try:
                    string = string + f"\n{self.notacion.devolver_indice("blanco",x)}\t\t{self.notacion.devolver_indice("negro",x)}"
                except:
                    string = string + f"\n{self.notacion.devolver_indice("blanco",x)}"
        elif pieza.color == "negro":
            if self.convertirse:
                if self.se_captura_pieza == "correcto":
                    self.notacion.agregar_movimiento(f"{pieza.tipo_color[0].upper()}{salida} x {llegada}",pieza.color)
                else:
                    if self.ennrrooqquuee == 0:
                        self.notacion.agregar_movimiento(f"{pieza.tipo_color[0].upper()}{llegada}\t",pieza.color)
                    elif self.ennrrooqquuee == 1:
                        self.notacion.agregar_movimiento(f"o-o\t",pieza.color)
                        self.ennrrooqquuee = 0
                    elif self.ennrrooqquuee == 2:
                        self.notacion.agregar_movimiento(f"o-o-o\t",pieza.color)
                        self.ennrrooqquuee = 0
            else:
                self.notacion.agregar_movimiento(f"P={pieza.tipo_color[0].upper()}{llegada}\t",pieza.color)
            for x in range(self.notacion.devolver_len(pieza.color)):
                string = string + f"\n{self.notacion.devolver_indice("blanco",x)}\t\t{self.notacion.devolver_indice("negro",x)}"
        return string
    
    def predecir1(self, pieza):
        def predecir2(pieza1, eli_casilla):
            l_b, l_n = buscar_mejora(pieza1,eli_casilla)
            if pieza1.casilla not in self.evaluados:
                self.var += 1
                lista_aristas = pieza1.movimiento_posibles(self.notacion.lista_notacion_blancos, self.notacion.lista_notacion_negros, l_b,l_n)
                self.evaluados.append(pieza1.casilla)
                lista_add = []
                try:
                    for cas in lista_aristas:
                        if cas not in self.recorridos:
                            lista_add.append(cas)
                    self.recorridos += lista_add
                    self.predict.agregar_nodos(lista_add)
                    self.predict.agregar_aristas(pieza1.casilla, lista_aristas)
                except Exception as e:
                    print("mal en prediccion 1 por " + e)
                try:
                    for i in lista_add:
                        pieza1.modify_casilla(i, self.lista_casillas)
                        predecir2(pieza1,eli_casilla)
                        self.var=0     
                except Exception as e:
                    print("mal por " + e)
                finally:
                    return
            else: 
                return 
        
        def  buscar_mejora(pi, eli_cas):
            l_b = self.lista_objetos.get_lista_blancos().copy()
            l_n = self.lista_objetos.get_lista_negros().copy()
            if pi.color == "blanco":
                for i in l_b:
                    if i.casilla == eli_cas:
                        l_b.remove(i)
                        break
                for i in l_n:
                    if i.casilla == pi.casilla:
                        l_n.remove(i)
                        break
                obj = Objetos(pi.casilla, pi.color ,pi.posicion_x,pi.posicion_y,self.get_pawn_blanco(),pi,pi.tipo_color)
                l_b.append(obj)
            if pi.color == "negro":
                for i in l_n:
                    if  i.casilla == eli_cas:
                        l_n.remove(i)
                        break
                for i in l_b:
                    if i.casilla == pi.casilla:
                        l_b.remove(i)
                        break
                obj = Objetos(pi.casilla, pi.color ,pi.posicion_x,pi.posicion_y,None,pi,pi.tipo_color)
                l_n.append(obj)
            return l_b, l_n
        
        self.predict = Prediccion()
        self.predict.agregar_nodos([pieza.casilla])
        self.recorridos = [pieza.casilla]
        self.evaluados = []
        self.var = 0
        try:
            predecir2(pieza,pieza.casilla)
        except  Exception as e:
            print("falla predecir2 " , e)
    
    def acciones_diferentes(self):
        var = pygame.mouse.get_pos()
        x = var[0]%75
        y = var[1]%75
        coordenada_casilla = (var[0]-x,var[1]-y)
        casilla_seleccionada=Funciones.buscar_valor(self.lista_casillas,coordenada_casilla)

        if self.inicio=="":
            self.inicio = casilla_seleccionada
        elif self.inicio != "" and self.fin == "" and casilla_seleccionada !=  self.inicio:
            self.fin  = casilla_seleccionada

            try:
                pieza = copy.deepcopy(self.lista_objetos.identificar_pieza(self.inicio))
                print ("Evaluando movimientos de ", pieza.tipo_color , " desde ",self.inicio , " Hasta ", self.fin)
                self.predecir1(pieza)

                lista_obj_cas = self.predict.short_path(self.inicio,self.fin)
                self.lista_objetivos = [self.lista_casillas[i] for i in lista_obj_cas]

            except Exception as e:
                self.inicio = ""
                self.fin = ""
                print("Fallo en Prediccion ", e)

        elif  self.inicio != "" and self.fin != "":
            self.inicio = ""
            self.fin = ""

    def fin_juego(self) -> None:
        pygame.display.quit



            


