N=int(input())
for i in range(N):
    dot_space=". "*(N-i-1)
    zero="0 "*(2*i+1)
    print(dot_space+zero+dot_space)
for j in range(1,N):
    dot_space=". "* j
    zer="0 "* (2*(N-j)-1)
    print(dot_space+zer+dot_space)

"""
input:5
output:
. . . . 0 . . . . 
. . . 0 0 0 . . . 
. . 0 0 0 0 0 . . 
. 0 0 0 0 0 0 0 . 
0 0 0 0 0 0 0 0 0 
. 0 0 0 0 0 0 0 . 
. . 0 0 0 0 0 . . 
. . . 0 0 0 . . . 
. . . . 0 . . . .

"""
