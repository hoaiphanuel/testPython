#input
print ("nhap so n :")
n= int(input())

#xuly

S=0
i=0
while (i<=n):
    S=S+i
    i=i+3



#output
print (S)

#xuly

S=0
i=0
while (i<=n):
    if(i%3==0):
        S=S+i
    i=i+1



#output
print (S)


S=0

for i in range(0,n+1,3):
    S=S+i
    print (S)

#output
print (S)
