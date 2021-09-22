a={"野菜 ":"季節",
   "キャベツ":"春",
   "ナス":"秋",
   "ハクサイ":"冬"}
for key,value in a.items():
    if value=="季節"or value=="春":
        print(key,":",value,sep="")