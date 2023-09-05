N=int(input())
c=65
for i in range(N):
    left_space=" "*(N-i-1)
    hallow=" "* (2*i-1)
    if i==0:
        print(left_space+chr(c))
        c+=1
    else:
        print(left_space+chr(c)+hallow+chr(c))
        c+=1
c-=2
for i in range(1,N):
    left_spac=" "* i
    hallow=" "*(2*(N-i-1)-1)
    if i==N-1:
        print(left_spac+chr(c))
    else:
        print(left_spac+chr(c)+hallow+chr(c))
        c-=1
  """
  input:5
  output:
    A
   B B
  C   C
 D     D
E       E
 D     D
  C   C
   B B
    A
  """
        
    
    
    
