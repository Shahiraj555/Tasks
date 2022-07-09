i=13
class stock:
    def __init__(self,name,pe,bv,cmp):
        self.a=  name
        self.b = pe
        self.c = bv
        self.d = cmp

    def cmp(self,current,bv):
        return self - self.c

ass1= stock('bajajconsumer',10,70,140)
ass2= stock('manappuram',10,97,99)
print(ass1.a,ass2.a)
print(ass1.b,' '*i, ass2.b)
print(self.cmp(140))

