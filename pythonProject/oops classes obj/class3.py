class person:


    def age(self,current_year,year_of_birth):
        return current_year - year_of_birth

    def mail(self,mailid):
        print('mail id is',mailid)

    def ask_name(self):
        name=input('tell your name')
        return name
    def dob(self):
        dob=input('tell your dob')
        return dob

sai=person()
raj=person()
sunny=person()

sai.mail('sai555@gmail.com')
print(sai.ask_name())
print(sunny.dob())


#
# t
#
# class sai:
#     def __init__(self,mail,name,city,state):
#         self.m=mail
#         self.n=name
#         self.c=city
#         self.s=state
#
# kartik=sai('kartik@hmail.com','kaartik','hari','punjab',)
# shami=sai('shami@gmail.com','shami','kopri','maharashtra')
#
# print(kartik.m)
# print(shami.n,shami.c)
# print(type(kartik))
# print(shami.c)
#


