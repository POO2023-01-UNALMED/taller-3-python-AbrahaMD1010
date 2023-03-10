class TV():
    
    
    numTV=0

    @classmethod
    def sumarTv(cls):
        cls.numTV+=1

    def __init__(self,marca,estado:bool) -> None:
        self._marca=marca
        self._estado=estado
        self.sumarTv()

        self._canal=1
        self._volumen=1
        self._precio=500
        self._control=None

    def setCanal(self,canal):
        if (canal>=1 and canal<=120 and self._estado==True):
            self._canal=canal
    def getCanal(self):
        return self._canal
    
    def setVolumen(self,volumen):
        if (volumen>=1 and volumen<=7 and self._estado==True):
            self._volumen=volumen
    def getVolumen(self):
        return self._volumen
    
    def setPrecio(self,precio):
        self._precio=precio
    def getPrecio(self):
        return self._precio
    
    def setMarca(self,marca):
        self._marca=marca
    def getMarca(self):
        return self._marca
    
    def setControl(self,control):
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