N=int(input())
for i in range(N):
    dots=". "*(N-i-1)
    zeros="0 "*(2*i+1)
    print(dots+zeros+dots*2+zeros+dots)
"""
input:3
output:
. . 0 . . . . 0 . . 
. 0 0 0 . . 0 0 0 . 
0 0 0 0 0 0 0 0 0 0
"""
