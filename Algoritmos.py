def ispalindromo(palabra):

    if isinstance(palabra,str) and len(palabra) > 2:
        return sorted(palabra[:len(palabra)//2]) == sorted(palabra[len(palabra)//2 + 1:])

def isanigrama(pal1, pal2):

    if (isinstance(pal1,str) and isinstance(pal2,str)):
        return sorted(pal1) == sorted(pal2)
