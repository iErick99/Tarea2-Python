from Algoritmos import isanigrama, ispalindromo

def test_isanigrama():
    a = 'hola'
    b = 'carro'
    assert isanigrama(a,b) == False, 'Error crítico'


def test_ispalindromo():
    a = 'hola'
    assert ispalindromo(a) == False, 'Error crítico'


def test_isanigrama2():
    a = 'car'
    b = 'arc'
    assert isanigrama(a, b) == True, 'Error crítico'


def test_ispalindromo2():
    a = 'arenera'
    assert ispalindromo(a) == True, 'Error critico'