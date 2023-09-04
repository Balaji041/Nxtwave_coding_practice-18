N=int(input())
S=float(input())
sum=0
for i in range(N):
    num=float(input())
    sum+=num
if round(sum,3)==S:
    print("True")
else:
    print("False")
"""
input:3
11.087
2.156
3.1415
5.7894
output:True
"""
