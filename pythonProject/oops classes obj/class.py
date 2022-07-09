# class stock:
#     pass
# hul=stock()
# hul.pe= 85
# hul.eps= 150
# hul.bookvalue=500
# hul.cmp=2100
#
# print(hul.cmp)
#
# mrf=stock()
# mrf.pe=25
# mrf.eps=2000
# mrf.bookvalue=25000
# print(hul.cmp,mrf.pe)

class Stock:
    def __init__(self,xyz,eps,cmp,bv):
        self.pe=xyz
        self.eps=eps
        self.cmp=cmp
        self.bv=bv

bajajcon = Stock(10,20,30,50)
manappuram= Stock(50,25,10,14)


print(manappuram.pe)



