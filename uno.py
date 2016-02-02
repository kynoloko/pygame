


import pygame
import pyganim



def main():

    pygame.init() # inicializo el modulo
    pantalla=pygame.display.set_mode((500,500))

    animacion=pyganim.PygAnimation([('1.png',100),('2.png',100),('3.png',100),('4.png',100)])


    animacion.play()





    pygame.display.set_caption("Mi Ventana") # Titulo de la Ventana
    #creo un reloj para controlar los fps

    reloj1=pygame.time.Clock()
    blanco=(255,255,255) # color blanco en RGB
    color2=(100,30,200)
    salir=False

    target=[0,0]

    #LOOP PRINCIPAL
    while salir!=True:
        #recorro todos los eventos producidos
        #en realidad es una lista
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                 target=event.pos


        reloj1.tick(18)#operacion para que todo corra a 20fps
        pantalla.fill(color2) # pinto la superficie de blanco
        animacion.blit(pantalla,target)

        pygame.display.update() #actualizo el display

    pygame.quit()

main()