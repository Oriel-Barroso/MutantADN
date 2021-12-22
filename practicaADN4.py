from time import time


class Mutant:
    def __init__(self, adn = None, saltoDiagonalDerecha = 0, saltoDiagonalIzquierda = 0, saltoVertical = 0, saltoHorizontal = 0, 
                stopDiagonalDerecha = 0, stopDiagonalIzquierda = 0, stopVertical = 0, stopHorizontal = 0) -> None:
        self.adn = adn
        self.saltoDiagonalDerecha = saltoDiagonalDerecha
        self.saltoDiagonalIzquierda = saltoDiagonalIzquierda
        self.saltoVertical = saltoVertical
        self.saltoHorizontal = 1
        self.stopDiagonalDerecha =  stopDiagonalDerecha
        self.stopDiagonalIzquierda = stopDiagonalIzquierda
        self.stopVertical = stopVertical
        self.stopHorizontal = 4

    @property
    def adn (self):
        return self._adn
    
    @adn.setter
    def adn(self, value):
        self._adn = value
    
    @property
    def saltoDiagonalDerecha(self):
        return self._saltoDiagonalDerecha
    
    @saltoDiagonalDerecha.setter
    def saltoDiagonalDerecha(self, value):
        self._saltoDiagonalDerecha = value
    
    @property
    def saltoDiagonalIzquierda(self):
        return self._saltoDiagonalIzquierda
        
    @saltoDiagonalIzquierda.setter
    def saltoDiagonalIzquierda(self, value):
        self._saltoDiagonalIzquierda = value

    @property
    def saltoVertical(self):
        return self._saltoVertical

    @saltoVertical.setter
    def saltoVertical(self, value):
        self._saltoVertical = value

    @property
    def saltoHorizontal(self):
        return self._saltoHorizontal

    @saltoHorizontal.setter
    def saltoHorizontal(self, value):
        self._saltoHorizontal = value

    @property
    def stopDiagonalDerecha(self):
        return self._stopDiagonalDerecha
        
    @stopDiagonalDerecha.setter
    def stopDiagonalDerecha(self, value):
        self._stopDiagonalDerecha = value

    @property
    def stopDiagonalIzquierda(self):
        return self._stopDiagonalIzquierda

    @stopDiagonalIzquierda.setter
    def stopDiagonalIzquierda(self, value):
        self._stopDiagonalIzquierda = value
    
    @property
    def stopVertical(self):
        return self._stopVertical
    
    @stopVertical.setter
    def stopVertical(self, value):
        self._stopVertical = value

    @property
    def stopHorizontal(self):
        return self._stopHorizontal

    @stopHorizontal.setter
    def stopHorizontal(self, value):
        self._stopHorizontal = value


    def checkADN(self, adn):
        contadorDiagonalDerecha, contadorDiagonalIzquierda, contadorHorizontal = 0, 0, 0
        cantidadFilasColumnas = round(len(adn) ** 0.5)
        punteroAntepenultimoValorPorFila = cantidadFilasColumnas - 3 
        punteroAntepenultimaFila = (cantidadFilasColumnas - 3) * cantidadFilasColumnas
        punteroUltimaPosicionEnFila = cantidadFilasColumnas - 1
        total = 0
        for i in range(0, len(self.adn)-3):
            if i < punteroAntepenultimaFila and contadorDiagonalDerecha < punteroAntepenultimoValorPorFila and \
            self.adn[i:self.stopDiagonalDerecha:self.saltoDiagonalDerecha] == self.adn[i]*4:
                print(self.adn[i:self.stopDiagonalDerecha:self.saltoDiagonalDerecha], 'A')
                total += 1
                print('A', i, 'total ', total)

            
            if i < punteroAntepenultimaFila and contadorDiagonalIzquierda >= 3 and \
            self.adn[i:self.stopDiagonalIzquierda:self.saltoDiagonalIzquierda] == self.adn[i]*4:
                print(self.adn[i:self.stopDiagonalIzquierda:self.saltoDiagonalIzquierda], 'B')
                total += 1
                print('B', i, 'total ', total)


            if contadorHorizontal < punteroAntepenultimoValorPorFila and self.adn[i:self.stopHorizontal:self.saltoHorizontal] == self.adn[i]*4:
                print(self.adn[i:self.stopHorizontal:self.saltoHorizontal], 'C')
                total += 1
                print('C', i, 'total ', total)


            if i < punteroAntepenultimaFila and self.adn[i:self.stopVertical:self.saltoVertical] == self.adn[i]*4:
                print(self.adn[i:self.stopVertical:self.saltoVertical], 'D')
                total += 1
                print('D', i, 'total ', total)


            if total > 1:
                return (True, total, i)

            if contadorHorizontal == punteroUltimaPosicionEnFila and contadorDiagonalDerecha == punteroUltimaPosicionEnFila \
            and contadorDiagonalIzquierda == punteroUltimaPosicionEnFila:
                contadorHorizontal = -1 #1
                contadorDiagonalDerecha = -1
                contadorDiagonalIzquierda = -1
            
            self.stopDiagonalDerecha += 1
            self.stopDiagonalIzquierda += 1
            self.stopHorizontal +=  1
            self.stopVertical +=  1
            contadorDiagonalDerecha +=  1
            contadorDiagonalIzquierda +=  1
            contadorHorizontal   +=  1
        return (False, total)


def main():
    listaADN = ['AAAAA', 'AAAAA', 'GCCAC', 'TAECA', 'TAECA']
    mutant = Mutant()
    mutantAdn = ''.join(listaADN)
    mutant.adn = mutantAdn
    cantidadFilasColumnas = round(len(mutant.adn) ** 0.5)
    mutant.saltoDiagonalDerecha = cantidadFilasColumnas + 1
    mutant.saltoDiagonalIzquierda = mutant.saltoDiagonalDerecha - 2
    mutant.saltoVertical = mutant.saltoDiagonalDerecha - 1
    mutant.saltoHorizontal = 1
    mutant.stopDiagonalDerecha = cantidadFilasColumnas * 4 
    mutant.stopDiagonalIzquierda = cantidadFilasColumnas * 3
    mutant.stopVertical = mutant.stopDiagonalDerecha
    mutant.stopHorizontal = 4
    print(len(listaADN))
    if len(mutantAdn) < 16:
        print('El largo de la lista debe ser mayor a 16')
    else:
        start_time = time()
        f = mutant.checkADN(mutant.adn)
        elapsed_time = time() - start_time
        print(f'En main {f} : ', elapsed_time)


if __name__ == '__main__':
    main()
