from typing import Counter


a=int(input("整数a: "))
b=int(input("整数b: "))
a,b=sorted([a,b]) #昇順

counter=a         #aをcounterにいれる
while counter<=b:
    print(counter,end="")
    counter=counter+1 #bまで繰り返す
print()

#list4-4
print("1からnまでの和を求めます")
while True:
    n=int(input("nの値:"))
    if n>0:
        break  #nが１以上で抜け出す nが-の場合は無限ループ
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("1から",n,"、までの和は",sum,"です")