import nu

entradas = [-1,7,5]
pesos = [0.8,0.1,0]

def soma(e,p):
    s=0
    for i in range(3):
        #print(e[i])
        #print(p[i])
        s += e[i] * p[i]
    return s
        
final = soma(entradas,pesos)

def stepfunction(soma):
    if(soma>=1):
        return 1
    return 0

r = stepfunction(final)