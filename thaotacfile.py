# Mở file để ghi
import  random as rd
import os

def docfile(tenfile):
    data=[]
    # Mở file để đọc dữ liệu
    with open(tenfile,'r', encoding='UTF-8') as file:
        line= file.read()
        sents = line.split(".")
        for ss in sents:
            data.append(ss)
    return data

def timkiem(data,text):
    for d in data:
        if text in d:
            return (1)
    return (0)

def timfile(dr,text):
    kq=[]
    allfiles = os.listdir(dr)
    for fi in allfiles:
        if(timkiem(docfile(dr+"/"+fi),text)):
            kq.append(fi)
    return kq


def them (data,text,n):
    #them dong text vào trong dữ liệu với n lần
    for i in range(n):
        data.insert(rd.randint(1,len(data)),text)
    return  (data)

def ghifile(tenfile,data):

    fo = open(tenfile, "w",encoding='UTF-8')
    for d in data:
        fo.write(d+". ")
    fo.close()


if __name__ == "__main__" :
    #làm marketing
    tfile = "./data/contentemarketing.txt"
    #a = docfile(tfile)
    ##print(a)
    ##a= them(a,"là con gái phải xinh",5)
    ##ghifile(tfile,a)
    #tim file co một từ nào đó
    b = timfile("./banan", " cướp")
    print(b)
#print (a)
