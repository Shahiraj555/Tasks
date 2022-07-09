class Stock:
    def __init__(sai,xyz,eps,cmp,bv):
        sai.pe=xyz
        sai.eps=eps
        sai.cmp=cmp
        sai.bv=bv

    def age(sai,current):
        return current - sai.bv

bajajcon = Stock(10,20,30,50)
manappuram= Stock(50,24,10,14)
sai=Stock(50,20,1,25)


# print(manappuram.eps , manappuram.pe)
# print(type(bajajcon))
print(sai.age(2000))
# print(bajajcon.age(2000))
