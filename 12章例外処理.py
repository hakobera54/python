try: #tryでエラーが起こった場合を想定
    a=int(input("整数を入力してください:"))
    if a==50:
        raise ValueError #50もエラーにしたい場合
    print(100//a)
except ZeroDivisionError: #エラーがおこるときの対応
    print("ゼロによる除算が行われました。")
except:
    print("何らかの例外が発生しました。")
else:
    print("正常終了") #エラーが起こらない場合
finally:
    print("お疲れさまでした") #エラーが起きても起きなくても