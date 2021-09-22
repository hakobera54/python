a=int(input("国語の点数を入力: "))
b=int(input("数学の点数を入力: "))
c=int(input("英語の点数を入力: "))
if a+b+c>=230:
    print("合格です")
elif a+b+c>=210 and a>=85 or b>=85 or c>=85:
    print("合格です")
else:
    print("補講です")

