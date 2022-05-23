
reflectores = [ 'EJMZALYXVBWFCRQUONTSPIKHGD',
              'YRUHQSLDPXNGOKMIEBFZCWVJAT',
              'FVPJIAOYEDRZXWGCTKUQSBNMHL']

conRotores = [ 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
            'AJDKSIRUXBLHWTMCQGZNPYFVOE',
            'BDFHJLCPRTXVZNYEIWGAKMUSQO',
            'ESOVPZJAYQUIRHXLNFTGKDCMWB',
            'VZBRGITYUPSDNHLXAWMJQOFECK',
            'JPGVOUMFYQBENHZRDKASXLICTW',
            'NZJHGRCXMYSWBOUFAIVLPEKQDT',
            'FKQHTLXOCBJSPDZRAMEWNIUYGV']

vueltaRotores = ['UWYGADFPVZBECKMTHXSLRINQOJ',
                  'AJPCZWRLFBDKOTYUQGENHXMIVS',
                  'TAGBPCSDQEUFVNZHYIXJWLRKOM',
                  'HZWVARTNLGUPXQCEJMBSKDYOIF',
                  'QCYLXWENFTZOSMVJUDKGIARPHB',
                  'SKXQLHCNWARVGMEBJPTYFDZUIO',
                  'QMGYVPEDRCWTIANUXFKZOSLHJB',
                  'QJINSAYDVKBFRUHMCPLEWZTGXO']

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def normalizarTexto(texto):
    resultado = ""
    texto = texto.replace(" ", "").upper()
    for letra in texto:
        if letra in alfabeto:
             resultado+=letra
    return resultado



def caracterPosicion(caracter):
    return int(ord(caracter)-65)



def cambio(caracter,charset=alfabeto,n=0):
    pos = caracterPosicion(caracter)+n
    caracter = charset[pos % 26]
    return caracter



class enigmaM3:
    reflector = ""
    rotores = ""
    plugboard = ""
    posInicio= ""
    posInterna = ('A','A','A')
    muesca = (('Q',),('E',),('V',),('J',),('Z',),('Z','M'),('Z','M'),('Z','M'))
    opts = []



    def __init__(self,rotor,ref,posInicio,posInterna,plugboard=None):
        self.setRotores(rotor)
        self.setReflector(ref)
        self.setPosInicio(posInicio)
        self.setPosInterna(posInterna)
        self.setPlugboard(plugboard)
        self.opts.append([rotor,ref,posInicio,posInterna,plugboard])



    def setReflector(self,caracter):
        self.reflector = reflectores[caracterPosicion(caracter)]


    def setRotores(self,rotor):
        rots = []
        for elemento in range(len(rotor)):
            rots.append(rotor[elemento]-1)
        self.rotores = tuple(rots)


    def setPosInicio(self,posInicio):
        self.posInicio = list(posInicio)


    def setPosInterna(self,posInterna):
        self.posInterna = (posInterna)


    def setPlugboard(self,plugboard):
        self.plugboard = plugboard


    def resetear(self):
        opts = self.opts[0]
        self.__init__(opts[0],opts[1],opts[2],opts[3],opts[4])


    def applyRotor(self,caracter,n,rotor):
        caracter = cambio(caracter,rotor,n)
        return cambio(caracter,n=-n)


    def reflecta(self,caracter):
        return cambio(caracter,self.reflector)


    def rotorAvanza(self):
        if self.posInicio[1] in self.muesca[self.rotores[1]]:
            self.posInicio[0] = cambio(self.posInicio[0],n=1)
            self.posInicio[1] = cambio(self.posInicio[1],n=1)
        if self.posInicio[2] in self.muesca[self.rotores[2]]:
            self.posInicio[1] = cambio(self.posInicio[1],n=1)
        self.posInicio[2] = cambio(self.posInicio[2],n=1)


    def applyPlugboard(self,caracter):
        for i in self.plugboard:
            if caracter == i[0]:
                return i[1]
            if caracter == i[1]:
                return i[0]
        return caracter


    def cifrarLetra(self,caracter):
        caracter = self.applyPlugboard(caracter)
        self.rotorAvanza()
        for i in range(2,-1,-1):
            n = ord(self.posInicio[i]) - ord(self.posInterna[i])
            caracter = self.applyRotor(caracter,n,conRotores[self.rotores[i]])
        caracter = self.reflecta(caracter)
        for i in range(3):
            n = ord(self.posInicio[i]) - ord(self.posInterna[i])
            caracter = self.applyRotor(caracter,n,vueltaRotores[self.rotores[i]])
        caracter = self.applyPlugboard(caracter)
        return caracter


    def cifrar(self,texto):
        output = ""
        for letra in texto:
            output += self.cifrarLetra(letra)
        return output


    def descifrar(self,texto):
        return self.cifrar(texto)



