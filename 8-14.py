#辞書
a={"野菜 ":"季節",
   "キャベツ":"春",
   "ナス":"秋",
   "ハクサイ":"冬"}
for key,value in a.items():
    print(key,":",value,sep="")