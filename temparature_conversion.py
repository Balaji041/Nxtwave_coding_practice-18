N=input()
l=len(N)
symbol=N[l-1:]
if (symbol=="k" or symbol=="K"):
    vales=float(N[:l-1])
    symbol=N[l-1:]
    c=vales-273
    k=vales
    f=(9*c/5)+32
    print(str(round(c,2))+"C")
    print(str(round(f,2))+"F")
    print(str(round(k,2))+"K")
    
if(symbol=="C"or symbol=="c"):
    vales=float(N[:l-1])
    c=vales
    k=vales+273
    f=(9*c/5)+32
    print(str(round(c,2))+"C")
    print(str(round(f,2))+"F")
    print(str(round(k,2))+"K")
if (symbol=="f"or symbol=="F"):
    vales=float(N[:l-1])
    c=(vales-32)*5/9
    k=c+273
    f=vales
    print(str(round(c,2))+"C")
    print(str(round(f,2))+"F")
    print(str(round(k,2))+"K")
    
    

"""
input:37.5F
output:
3.06C
37.5F
276.06K
"""
