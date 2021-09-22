moji="abc"+"def"
print(moji)

moji="-"*10
print(moji)

s="abcdef"
print(len(s)) #len関数は文字列の長さを取ってこれる

s="abcdef"
print(s[0:3]) #添え字の0~3を取ってくる

n="abcdef"
if "bc" in n:
    print(n)

n="abcdef"
for i, ch in enumerate(n): #添え字と文字列をとってくる
  print(i,ch)

n="abcdef"
print(n.index("cd")) #indexで指定したの添え字をとってくる

a=10
b=20
print("こんに{ka}ちは".format(ka=a)) #aをkaに指定
