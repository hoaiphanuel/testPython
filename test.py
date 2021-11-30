
#h100 dau * tren 1 hàng
#print("*"*100)
# một hình chữ nhật 10x10
print((("*"*10)+"\n")*(2*5))
a=[1,2,3,4,5,6,7,8,3,8,4,4,4,4]
for i in range(len(a)):
        for j in range(len(a)):
                if (a[i]<a[j]):
                        tam=a[i]
                        a[i]=a[j]
                        a[j]=tam
print(a)


def sapxep(a):
    for i in range(len(a)):
        for j in range(len(a)):
                if (a[i]<a[j]):
                        tam=a[i]
                        a[i]=a[j]
                        a[j]=tam
    return (a)
def timkiem(a):
        return (a)
