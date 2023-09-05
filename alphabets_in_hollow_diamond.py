N=int(input())
A=65
for i in range(1,N+1):
    left_space=" "*(N-i)
    if i!=1:
        hollow=" "*(2*i-3)
        print(left_space+chr(A)+hollow+chr(A+1))
        A+=2
    else:
        print(left_space+chr(A))
        A+=1
A-=3
for j in range(1,N):
    left_spac=" "*(j)
    hollow=" "*(2*(N-j)-3)
    if j==N-1:
        print(left_spac+chr(A))
    else:
        print(left_spac+chr(A-1)+hollow+chr(A))
        A-=2
"""
input:7
output:
      A
     B C
    D   E
   F     G
  H       I
 J         K
L           M
 J         K
  H       I
   F     G
    D   E
     B C
      A
"""
