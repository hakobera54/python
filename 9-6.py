def a(sum):
    """ 引数に指定された数値配列の全要素を合計した値を返却する """
    # 合計値の初期化
    total = 0

    # 配列の要素数分ループ
    for i in range(len(sum)):
        num = sum[i]

        # 整数値の場合のみ合算する
        if type(num) is int:
            total += num
    
    return total

# メイン処理

# 配列の初期化
nums = [4,10,59,679,1991,3994,6789,19324]

# 合計値を求める関数（メソッド）を呼び出し結果を表示
total = a(nums)
print("合計値 =", total)
