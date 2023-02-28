class Marca():
    def __init__(self,nombre:str) -> None:
        self._nombre=nombre

    def getNombre(self):
        return self._nombre  
    def setNombre(self,nombre):
        self._nombre=nombre

class TV():
    _canal=1
    _volumen=1
    _precio=500
    _control=None
    numTV=0

    def __init__(self,marca:Marca,estado:bool) -> None:
        self._marca=marca
        self._estado=estado
        numTv+=1
    
    def setCanal(self,canal):
        if (canal>=1 and canal<=120):
            self._canal=canal
    def getCanal(self):
        return self._canal
    
    def setVolumen(self,volumen):
        if (volumen>=1 and volumen<=7):
            self._volumen=volumen
    def getVolumen(self):
        return self._volumen
    
    def setPrecio(self,precio):
        self._precio=precio
    def getPrecio(self):
        return self._precio
    
    def setMarca(self,marca:Marca):
        self._marca=marca
    def getMarca(self):
        return self._marca
    
    def setControl(self,control:Control):
        self._control=control
    def getControl(self):
        return self._control
    
    @classmethod
    def setNumTV(cls,num):
        cls.numTV=num
    @classmethod
    def getNumTV(cls):
        return cls.numTV
    
    def getEstado(self):
        return self._estado
    
    #metodos
    def turnOn(self):
        self._estado=True
    def turnOff(self):
        self._estado=False

    def canalUp(self):
        if(self._estado==True):
            if(self._canal>=1 and self._canal<120):
                self._canal+=1
    def canalDown(self):
        if(self._estado==True):
            if (self._canal>1 and self._canal<=120):
                self._canal-=1
            
    def volumenUp(self):
        if(self._estado==True):
            if(self._volumen>=1 and self._volumen<7):
                self._volumen+=1
    def volumenDown(self):
        if(self._estado==True):
            if(self._volumen>1 and self._volumen<=7):
                self._volumen-=1

class Control():
    tv=None

    def enlazar(self,tv:TV):
        tv.setControl(self)
        self.tv=tv

    def turnOn(self):
        self.tv.turnOn
    def turnOff(self):
        self.tv.turnOff
    
    def canalUp(self):
        self.tv.canalUp
    def canalDown(self):
        self.tv.canalDown

    def volumenUp(self):
        self.tv.volumenUp
    def volumenDown(self):
        self.tv.volumenDown
    
    def setCanal(self):
        self.tv.setCanal
        
        


    
        