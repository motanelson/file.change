import os
import copy


print("\033c\033[47;31m\ngive me the file to change ? ")
a=input().strip()
print("give me \n0 to add string to start of line\n1 to add string to end of line ? \n")
b=input().strip()
b=int(b)
if b>1 or b<0:
    exit(1)
print("give me a sting to add \\n to enter ?\n")
c=input()
c=c.replace("\\n","\n")
c=c.replace("\\r","\r")
c=c.replace("\\t","\t")
f1=open(a,"r")
f=f1.read()
f1.close()
ff=f.split("\n")
sss=""
for h in ff:
    if b==0:
        sss=sss+c+h+"\n"
    else:
        sss=sss+h+c+"\n"
f1=open(a,"w")
f1.write(sss)
f1.close()
