import pandas as pd
data=pd.read_csv("./data/bangtraphongthuy.csv")
#print(data)
def ketqua(tra):
    return (" thông tin ra được là "+ data["Ý NGHĨA"][tra]+" ----" + data["KẾT LUẬN"][tra])
#print (ketqua(4))
key="N"
while (key.upper()!="Y"):
    sdt=input()
    sdt=sdt[-4:]
    tra=int(sdt)%80
    print(ketqua(tra))
    print("\n bạn có muốn thoát hay không?Y/N")
    key=input()

