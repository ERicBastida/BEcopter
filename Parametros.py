import openpyxl

class GestParametros():
    def __init__(self,pathDocument,nSheet):
        try:
            self.__doc = openpyxl.load_workbook(pathDocument)
        except:
            print "No se ha podido cargar los datos"
        else:
            try:
                Hoja = self.__doc[( self.__doc.sheetnames[nSheet])]
            except IndexError:
                self.ListParam = []
            else:

                self.ListParam = []

                for r in Hoja.rows:
                    paramTemp = Parametro()
                    #Se carga toda la informacion de una linea para almacenarlo en un parametro
                    if r[0].value != "Per." and r[0].value != None:

                        paramTemp.setPermit(r[0].value)
                        paramTemp.setCode(r[1].value)
                        paramTemp.setName(r[2].value)
                        paramTemp.setDescription(r[3].value)
                        paramTemp.setIncrement(r[5].value)
                        paramTemp.setRange(r[4].value)



                        paramTemp.setUnits(r[6].value)
                        self.ListParam.append(paramTemp)

    def getParams(self,key=None):
        if key == None:
            return self.ListParam
        else:

            for p  in self.ListParam:

                if p.getCode() == key:
                    return p
            return []

    def setParam(self,LP):
        pass
    def save(self):
        pass







class Parametro():
    """
    Objeto que contiene toda la informacion perteneciente a un parametro

    obs: Recibe todo en string
    permit = W o R  (W = Can Write , R= Read only)
    code = CODE_PARAM_IN_VEHICLE
    name = "Name Param"
    description = "Description txt"
    range = "r1,r2" -> convert to -> [r1, r2]

    """
    def __init__(self, permit=None,code=None,name=None,description=None,range=[0,0],increment=None,units=None):
        self.__per   = permit         #Permiso para modificar o leer unicamente (W o R)
        self.__cod   = code           #Codigo/Key para buscar el parametro
        self.__name  = name           #Nombre descriptivo del parametro
        self.__desc  = description    #Descripcion del parametro y sus correspondientes valores/significados
        self.__range = range          #Rango de valores que puede tomar el parametro. Esto sirve para representar el slider
        self.__incre = increment      #Incremento de valores que puede tomar el parametro y aceptar el firmware
        self.__units = units          #Unidad del parametro. Por ejemplo, Hz, PWM, metros/segundos, etc.

        self.__hasRange = False       #Bandera para saber si tiene o no un rango y para implementar su respectivo slider
        self.__is_float = False       #En caso de ser
        self.__scale = 1

    def setPermit(self,p):
        self.__per = p
    def setCode(self,c):
        self.__cod = c
    def setName(self,n):
        self.__name= n
    def setDescription(self,d):
        self.__desc=d
    def setRange(self,r):
        try:

            if r != None:
                self.__hasRange = True
                r1,r2=r.split(',')

                condicion = ('.' in r1) or ('.' in r2) or (isinstance(self.__incre, float))

                #Pregunto primero si son valores flotanes o enteros, para utilizar la funcion respectiva.
                if condicion:

                    decimal1 = r1.split('.')[1] if len(r1.split('.')) > 1 else '0'
                    decimal2 = r2.split('.')[1] if len(r2.split('.')) > 1 else '0'
                    decimal3 = str(self.__incre).split('.')[1] if len(str(self.__incre).split('.')) > 1 else '0'
                    n = max(decimal1.__len__(),   decimal2.__len__(), decimal3.__len__()     )

                    self.__scale = int('1'+'0'*n )

                    self.__range = [float(r1), float(r2)]
                    self.__is_float= True
                else:
                    self.__range = [int(r1),int(r2)]

        except:
            AttributeError("Hubo un error al cargar el parametro. " + self.__cod)

    def setIncrement(self,i):
        try:
            if i != None :

                if isinstance(i, long):
                    self.__incre = int(i)
                else:
                    self.__incre = float(i)
                    self.__is_float= True
        except:
            self.__incre = 0
            self.__units = "Hubo un error al cargar el parametro."

    def setUnits(self,u):

        if u == None:

            self.__units = ""
        else:
            self.__units=u

    def getPermit(self):
        return self.__per
    def getCode(self):
        return self.__cod
    def getName(self):
        return self.__name
    def getDescription(self):
        return self.__desc
    def getRange(self):
        return self.__range
    def getIncrement(self):
        return self.__incre
    def getUnits(self):
        return self.__units
    def isFloat(self):
        "Si tiene algun atributo de tipo flotante"
        return self.__is_float
    def getScale(self):
        "En caso de tener atritubos de tipo flotantes, esta funcion envia cuantos digitos hay despues de la coma"
        return self.__scale

    def hasRange(self):
        return self.__hasRange
    def getObj(self):
        return self
if __name__ == '__main__':
    GP = GestParametros('data/configParameters.xlsx',0)
    Lista = GP.getParams()
