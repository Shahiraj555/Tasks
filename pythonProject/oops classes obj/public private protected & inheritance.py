from utility.utility1 import person2
obj=person2('sai','saheb',1555)
print(obj.y)
import class5
print(class5)
obj3= class5.person1('sai','lakade',1695)
print(obj3.y)
print(obj3._n)
print(obj3._person1__s)
class person :

    _name = "sudh"
    __surname = "kumar"
    yob = 1990

    def _age(self,current_year):
        return current_year - self.yob

    def __age1(self,current_year):
        return current_year - self.yob



obj = person()
print(obj._age(2000))
print(obj._person__age1(2022))

class employee(person) :
    _name = "sudhanshu"
    __surname = "singh"
    yob = 1991

obj1 = employee()
print(obj._age(2022))
print(obj1._name)
print(obj1._employee__surname)
print(obj1._person__age1(2022))