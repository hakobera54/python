a=[]
b=[]
for i in range(10):
    num=int(input(str(i+1)+"件目:整数を入力"))
    if num%2==0:
        a.append(num)
    else:
        b.append(num)
print("偶数値リスト=",a)
print("奇数値リスト=",b)