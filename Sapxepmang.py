import  random as rd
def doicho(m, n):
    return n, m
class Cmang:
    spt = 0
    tappt = []
    def __init__(self):
        self.spt = 100
        for i in range(self.spt):
            self.tappt.append(i)

    def taomang(self,n):
        self.tappt=[]
        self.spt = n
        for i in range(n):
            self.tappt.append(rd.randint(0,100))

    def showCmang(self):
        return self.tappt
    def sapxep(self):
        return 0

    def quicksort(self,L, R):
        if L >= R:
            return
        i = L
        j = R
        x = self.tappt[(L + R) // 2]
        while True:
            while (self.tappt[i] < x):
                i = i + 1
            while self.tappt[j] > x:
                    j = j - 1
            if i <= j:
                self.tappt[i], self.tappt[j] = doicho(self.tappt[i], self.tappt[j])
                i = i + 1
                j = j - 1
            else:
                break
        self.quicksort(L, j)
        self.quicksort(i, R)


a=Cmang()
a.taomang(50)
print (a.showCmang())
a.quicksort(0,a.spt-1)
print (a.showCmang())



