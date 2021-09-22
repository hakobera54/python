a={"id":100,
   "name":"大原太郎",
   "age":19}
a.update(age=20)
for key,value in a.items():
    print(key,":",value,sep="")