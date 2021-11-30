import pandas as pd
df = pd.read_csv("data/dulieu.csv", encoding='utf8')

def trave(gtri):
    return (df["caubinh"][gtri]+" số điện thoại này "+df["binh"][gtri])
kt="N"
while(kt.upper() != "Y"):
    so=input()
    tra=int(so[-4:])%80
    print(tra)
    print (trave(tra))
    print (" bạn có muốn thoat không?Y/N")
    kt=input()

