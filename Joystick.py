import pygame
import os


class Joystick(): #Extendera de la clase joystick
    old = False
    def __init__(self):
        "Se inicializan los modulos de joystick proporcionados por pygame"

        print "Se inicio el JOYSTICK"
        self.__buttons = {
            0 :  '',        #Button 0
            1 :  '',        #Button 1
            2 :  '',        #Button 2
            3 :  '',        #Button 3
            4 :  '',        #Others buttons - to be implemente
            5 :  '',
            6 :  '',
            7 :  '',
            8 :  '',
            9 :  '',
            10 : '',
            11:  '',
            12 : '',        #Axis 0
            13 : '',        #Axis 1
            14 : '',        #Axis 2
            15 : '',        #Axis 3
            16 : '',        #is Inverted Axe 0
            17 : '',        #is Inverted Axe 1
            18 : '',        #is Inverted Axe 2
            19 : ''         #is Inverted Axe 3
         }

        self.__on = False


    def conectados(self): #Debe ser un diccionario la concha de la lora
        "Diccionario con los id/nombres de los joysticks conectados."
        pygame.display.quit()
        pygame.joystick.quit()

        pygame.display.init() #Inicializamos el moduclo de display ya que joystick depende de este
        pygame.joystick.init()#Inicializamos el modulo de joystick que controla los comandos conectados a la pc

        d = dict()
        n = range(pygame.joystick.get_count())

        for x in n:
            id = pygame.joystick.Joystick(x).get_id()

            d[x] = pygame.joystick.Joystick(x).get_name()
        return d

    def seleccionarJoy(self,id):
        self.j = pygame.joystick.Joystick(id)
        self.j.init()
        self.__nombre = self.j.get_name()
        self.__cantBu = self.j.get_numbuttons()
        self.__cantEj = self.j.get_numaxes()
        self.__id = self.j.get_id()
        self.__on = self.j.get_init()

        filepath="./data/"+self.__nombre+".txt"
        print "Entraste a cargar lso datos del jooystick"
        if ( os.path.isfile(filepath)):
            print "Se encontraron configuraciones del joystick"
            self.old = True
            with open(filepath) as fp:
                line = fp.readline()
                while line:
                    altaLinea=  line.split(",")

                    if altaLinea != ['\n']:
                        key = altaLinea[0]
                        key = int(key)
                        action = altaLinea[1]
                        if action == ' \n':
                            action = ""
                        if action != "":
                            action = action[:-1]

                        if key > 15:

                            if action == "False":
                                action = False
                            else:
                                action =True

                        self.__buttons[key]=action

                    line = fp.readline()
            fp.close()

            print "Configuracion cargada : ", self.__buttons


        if self.old:
            return self.__buttons



    def obt_cantBotones (self):
        "Segun el joystick seleccionado enviar la cantidad de botones del mismo"
        return self.__cantBu

    def obt_nombre(self):
        "Se obtiene el nombre del comando conectado"
        nombre = "No se ha asignado un joystick."
        if self.obt_estado():
            nombre = self.__nombre
        return nombre

    def obt_info(self):
        return "ID: "+str(self.__id)+" - Nombre: "+self.__nombre+"- Cantidad de botones: "+str(self.__cantBu)+" - Cantidad de ejes: "+str(self.__cantEj)

    def obt_estado(self):
        "Indica que la clase joystick ya tiene uno asignado"
        return self.__on

    def desconectar(self):
        self.j.quit()

    def agr_mapeo(self,id, action):

        self.__buttons[id]= action

    def saveMap(self):

        filepath = 'data/' + self.__nombre + '.txt'
        with open(filepath,'w') as fp:
            for d  in self.__buttons:
                saveLine = str(d) + ","+ str(self.__buttons[int(d)]) +"\n"
                fp.write(saveLine)
            fp.close()


    def obt_mapeo(self,id):

        if id == -1:
            return self.__buttons
        elif id < self.__buttons.__len__():
            return self.__buttons[id]
        else:
            return None





