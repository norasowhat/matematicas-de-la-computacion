a=int(input("dame el valor de a: "))
b=int(input("dame el valor de b: "))

def maximoComunDivisor(a,b):

    c=abs(a)
    d=abs(b)

    while(d!=0):
        r=c%d
        c=d
        d=r
    return c
    

mcd=maximoComunDivisor(a,b)
print("------máximo común divisor-----")
print(f"mcd({a},{b})={mcd}")

def divisionEntera(a,b):
    if a==0:
        cociente=0
        residuo=0
    else:
        r=abs(a)
        q=0
        while(r>=b):
            r=r-b
            q=q+1
        if a>0:
            cociente=q
            residuo=r
        elif r==0:
            cociente=-q
            residuo=0
        else:
            cociente=-q-1
            residuo=b-r
    return cociente,residuo

print("-----resultados división entera-----")
print(f"cociente: {divisionEntera(a,b)[0]}")
print(f"resiudo:{divisionEntera(a,b)[1]}")
            




