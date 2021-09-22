class Circle:
    PI=3.1415
    def __init__(self,hankei:int,pai:int)->None:
        self.pai=pai
        self.hankei=hankei*hankei*pai
        

    def print(self)->None:
        print("{} {} {}".format(self.hankei,self.pai))
hankei=Circle(int(input("半径を整数値で入力:")))
pai=Circle(3.14)

hankei.print()
pai.print()
        