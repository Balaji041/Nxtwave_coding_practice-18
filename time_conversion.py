Time=input()
l=len(Time)
char=Time[l-1:]
num=0
if char=="M":
    char_num=int(Time[:l-1])
    num=round((char_num/60),2)
elif char=="S":
    char_num=int(Time[:l-1])
    num=round((char_num/3600),2)
print(str(num)+"H")
    
