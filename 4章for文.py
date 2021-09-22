n=int(input("挨拶は何回:"))
for i in range(1,n+1): #iは0からはじまる 1以上n+1未満
    print("No.",i,":ｌこんにちは")

#list4-12
start=int(input("開始："))
end=int(input("終了："))
step=int(input("増分"))
for count in range(start,end,step): #初期値､終了値､増分
    print(count,end=" ")
print()

#list4-17
print("-"*27)
for i in range(1,10):
    for j in range(1,10):
        print("{:3d}".format(i*j),end="")
    print()
print("-"*27)