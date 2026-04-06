# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    discriminante = (b ** 2) - (4 * a * c)
    if a != 0:
        if discriminante < 0:
            raiz = "( )"
        elif discriminante == 0:
            resolvente = (-1 * b) / (2 * a)
            raiz = f"({resolvente})"
        else : 
            resolvente1 = ((-1 * b) + discriminante ** (1/2)) / (2 * a) 
            resolvente2 = ((-1 * b) - discriminante ** (1/2)) / (2 * a)
            raiz = f"({resolvente1}, {resolvente2})"
    else: None
    return raiz


def value_y(a, b, c, x):
    cuadratica = (a * x ** 2) + (b * x) + c
    return int(cuadratica)


def to_string(a, b, c):
    
    if a != 0 and b !=0 and c !=0:
        polinomica = f"f(x) = {int(a)} * X^2 + {int(b)} * X + {int(c)}"
    elif a !=0 and b !=0 and c ==0:
        polinomica = f"f(x) = {int(a)} * X^2 + {int(b)} * X"
    elif a !=0 and b ==0 and c !=0:
        polinomica = f"f(x) = {int(a)} * X^2 + {int(c)}"
    elif a ==0 and b ==0 and c ==0:
        polinomica = ""
    elif a ==0 and b !=0 and c !=0:
        polinomica = f"f(x) = {int(b)} * X + {int(c)}"
    elif a ==0 and b !=0 and c ==0:
        polinomica = f"f(x) = {int(b)} * X"
    elif a ==0 and b ==0 and c !=0:
        polinomica = f"f(x) = {int(c)}"
    elif a !=0 and b ==0 and c ==0:
        polinomica = f"f(x) = {int(a)} * X^2"

    return polinomica


def derivation(a, b, c):

    if a !=0 and b!=0 : 
        derivada = f"f'(x) = {int(2 * a)} * X + {int(b)}"
    elif a==0 and b==0 :
        derivada = "f'(x) = 0"
    elif a!=0 and b==0:
        derivada = f"f'(x) = {int(2 * a)} * X"
    elif a==0 and b!=0:
        derivada = f"f'(x) = {int(b)}"

    return derivada


# a = float(input())
# b = float(input())
# c = float(input())
# x = float(input())
# print(roots(a, b, c))
# print(value_y(a, b, c, x))
# print(to_string(a, b, c))
# print(derivation(a, b, c))