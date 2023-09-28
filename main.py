def main():
    dato = -55
    es_complex(dato)
    es_booleano(dato)
    es_string(dato)
    es_entero(dato)
    es_flotante(dato)

def es_complex(x):
    if type(x) == complex:
        if x.real != 0:
            print(f'{x} es un número complejo híbrido')
        else:
            print(f'{x} es un número imaginario puro')
    else:
        pass

def es_booleano(x):
    if type(x) == bool:
        print(f'{x} es un dato booleano')
    else:
        pass

def es_string(x):
    if type(x) == str:
        print(f'{x} es una cadena de texto')
    else:
        pass

def es_entero(x):
    if type(x) == int:
        while x != 0:
            if x > 0:
                for n in range(2, x):
                    if x % n == 0:
                        print(f'{x} es un entero,positivo y es par')
                        break
                    else:
                       print(f'{x} es un entero,positivo e impar')
                       break
            else:
                print(f'{x} es un entero y es negativo')
            break
    else:
        pass

def es_flotante(x):
    if type(x) == float:
        while x != 0:
            if x > 0:
                print(f'{x} es un flotante y es positivo')
                break
            else:
                print(f'{x} es un flotante y es negativo')
                break
    else:
        pass
    
main()
