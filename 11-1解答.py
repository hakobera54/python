import math


class Circle:
    PI=3.1415
    def calc_cir(self,radius):
        res=2*Circle.PI*radius
        return math.floor(res*10**3)/(10**3)
    
    def area(self,radius):
        res=Circle.PI*radius**2
        return math.floor(res*10**3)/(10**3)

class Main:

    def execute(self):
        circle=Circle()
        radius=int(input("半径を整数値で入力:"))
        br=circle.calc_cir(radius)

        ar=circle.area(radius)
        print("円周の長さは{}です".format(br))
        print("円の面積は{}です".format(ar))
main=Main()
main.execute()