def Hello(): #関数を作る
    n=10
    for _ in range (n):
        print("hello")
Hello() #関数を呼び出す

#9-1
def schoo1_name(school,name):
    print("学校名:",school)
    print("名前:",name)
    return "完了"

school="東京情報クリエイター工学専門学校"
name="竹井一馬"
schoo1_name(school,name)

#リストを受け取る関数
def kansu(hensu2):
    hensu2+=1

hensu1=100
kansu(hensu1)
print(hensu1) #イミュータブルだから101にならない

def kansu(hensu2):
    hensu2[0]+=1

hensu1=[100]
kansu(hensu1)
print(hensu1[0]) #リストはミュータブルだから変更される

#複数の値の返却
def kansu():
    a=100
    b=200
    return a,b

print(kansu())

def kansu():
    a=100
    b=100
    return a,b
x,y=kansu()
print(x)


#メイン処理を上に書くために
def main():
    x,y=kansu()

def kansu():
    a=100
    b=200
    return a,b
if __name__=="__main__":
    main()