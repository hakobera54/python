n=int(input("現在の西暦を入力してください:"))
if n%4==0 or n%400==0:
   print("閏年です")
elif n%100==0:
   print("平年です")