N=int(input())
A=65
for i in range(N):
    space=" "*(N-i-1)
    hallow=" "*(2*i-1)
    if i==0:
        print(space+chr(A)+" "+space*2+chr(A))
        A+=1
    else:
        print(space+chr(A)+hallow+chr(A)+" "+space*2+chr(A)+hallow+chr(A))
        A+=1
        

"""
input:3
output:
  A     A
 B B   B B
C   C C   C
"""
