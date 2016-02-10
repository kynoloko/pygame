

import pygame
import pyganim




# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
r1=pygame.Rect(200,200,100,100)

#imagen=pygame.image.load("2.png")
#imagen2=pygame.image.load("gif_izquierda")



#def dibujacarro(pantalla ,x,y):
    #pantalla.blit(imagen,(x,y))





# Inicio
pygame.init()

# Establecemos el largo y alto de la pantalla [largo,alto]
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Mi Juego")

#Iteramos hasta que el usuario pulsa el botón de salir.
hecho = False

# Usamos esto para gestionar cuán rápido se actualiza la pantalla.
reloj = pygame.time.Clock()

# Ocultamos el cursor del ratón.
#pygame.mouse.set_visible(0)


# Velocidad y poscision para el ogro
x_speed = 0
y_speed = 0


x_coord = 5
y_coord = 5

#velocidad y poscicion para el rectangulo
rect_x=0
rect_y=0
#variables para posicion
pos_rect_x=1
pos_rect_y=1

#cordenadas para ogro2
ogro2pos_x=50
ogro2pos_y=50



anima=pyganim.PygAnimation([('1.png',100),('2.png',100),('3.png',100),('4.png',100)])
anima.play()

anima2=pyganim.PygAnimation([('1_izq.png',200),('2_izq.png',200),('3_izq.png',200),('4_izq.png',200)])
anima2.play()

# -------- Bucle Principal del Programa -----------
while not hecho:
    #TODO EL PROCESAMIENTO DE EVENTOS DEBERÍA IR DEBAJO DE ESTE COMENTARIO
    for evento in pygame.event.get():  # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
            hecho = True               # Marca que ya lo hemos hecho, de forma que abandonamos el bucle


            # El usuario presiona una tecla

        elif evento.type == pygame.KEYDOWN:
            # Mira si ha sido una de las flechas. Si es así
            # ajusta la velocidad.
            if evento.key == pygame.K_LEFT:
                x_speed =- 3
            elif evento.key == pygame.K_RIGHT:
                x_speed = 3
            elif evento.key == pygame.K_UP:
                y_speed =- 3
            elif evento.key == pygame.K_DOWN:
                y_speed = 3

        # El usuario deja de presionar la tecla
        elif evento.type == pygame.KEYUP:
            # Si es una de las flechas, resetea el vector a cero.
            if evento.key == pygame.K_LEFT:
                x_speed = 0
            elif evento.key == pygame.K_RIGHT:
                x_speed = 0
            elif evento.key == pygame.K_UP:
                y_speed = 0
            elif evento.key == pygame.K_DOWN:
                y_speed = 0

    # TODO EL PROCESAMIENTO DE EVENTOS DEBERÍA IR ENCIMA DE ESTE COMENTARIO

    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR DEBAJO DE ESTE COMENTARIO

    # Desplaza al objeto según el vector velocidad.
    x_coord += x_speed
    y_coord += y_speed




    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR ENCIMA DE ESTE COMENTARIO

    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO

    # Primero, limpiamos la pantalla con color blanco. No pongas otros comandos de dibujo
    # encima de esto, de lo contrario serán borrados por el comando siguiente.
    pantalla.fill(BLANCO)

    #dibujacarro(pantalla,x_coord,y_coord)

    anima.blit(pantalla,(x_coord,y_coord))
    anima2.blit(pantalla,(ogro2pos_x,ogro2pos_y))
    pygame.draw.rect(pantalla,VERDE,[rect_x,rect_y,40,40])


    rect_x+=pos_rect_x
    rect_y+=pos_rect_y


    if rect_x > 660 or rect_x< 0:
        pos_rect_x = pos_rect_x * -1
    if rect_y >460 or rect_y<0:
        pos_rect_y=pos_rect_y*-1

    if x_coord>660 or x_coord<0:
        x_speed=x_speed*-1
    if y_coord>460 or y_coord<0:
        y_speed=y_speed*-1





    pygame.draw.rect(pantalla,ROJO,r1)


    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO

    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # Limitamos a 60 fotogramas por segundo
    reloj.tick(60)

# Pórtate bien con el IDLE.
# Si nos olvidamos de ésta línea, el programa se 'colgará'
# en la salida.
pygame.quit()