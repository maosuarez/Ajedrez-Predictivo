from Estructura import *

bool1 = Funciones.LogIn()
if bool1:
    blancas, negras = Funciones.ElegirPiezas()
else:
    blancas = ["peon","alfil","caballo","rey"] 
    negras = ["torre","rey","peon","peon"]
Funciones.mostrar_piezas(blancas,negras)
casillas_blancas, casillas_negras = Funciones.elegir_casillas(blancas,negras)
juego = PyJuego()
juego.piezas_iniciales(blancas, negras, casillas_blancas, casillas_negras)
Activado = True
while Activado:
    juego.pantalla.blit(juego.fondo,(0,0))
    juego.romper = False
    if juego.convertirse:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Activado=False
                juego.fin_juego()
            if event.type == pygame.MOUSEBUTTONDOWN and  event.button == 1:
                juego.lista_objetivos = []
                juego.acciones_principales()
            if event.type == pygame.MOUSEBUTTONDOWN and  event.button == 3:
                juego.acciones_diferentes()
        Funciones.mostrar_pieza(juego.lista_objetos,juego.pantalla)
        Funciones.mostrar_objetivos(juego.pantalla, juego.lista_objetivos, juego.get_objetivo())
    else:
        juego.promocion()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Activado = False
                juego.fin_juego()
            if event.type == pygame.MOUSEBUTTONDOWN:
                juego.accion_promover()
    

    pygame.display.update()