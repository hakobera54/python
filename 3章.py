n=int(input("整数値: "))
if n>0:
    print("その値は正です。")
else:
    print("その値は0か負です。")

n=int(input("0~100までの得点(整数値)を入力してください: "))
if n>80:
    print("合格です ")

n=int(input("正の数値: "))
if n>0:
    if n%2==0:
        print("その値は正の偶数です")
    else:
        print("その値は正の奇数です")
else:
    print("正でない値が入力されました")
