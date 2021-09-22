foo="hello"
print(type(foo))
#整数＝int型,浮動小数=float型,文字=str型

bar=10.55
print(bar,type(bar))
#四捨五入する
bar=round(bar)
print(bar,type(bar))

foo=10
foo=foo<<1   #fooを１ビット左シフト
foo=bin(foo) #２進数に変換
print(foo)   #0b = ２進数