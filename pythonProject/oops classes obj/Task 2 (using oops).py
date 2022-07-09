# l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
# 1 . Try to reverse a list
# 2. try to access 234 out of this list
# 3 . try to access 456
# 4 . Try to extract only a list collection form list l
# 5 . Try to extract "sudh"
# 6 . Try to list all the key in dict element avaible in list
# 7 . Try to extract all the value element form dict available in list

l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]

import logging as lg                                       # 1 . Try to reverse a list
lg.basicConfig(filename='list.spy',level=lg.DEBUG, format= '%(asctime)s %(message)s')
class list_le:
    def __init__(self,s):
        self.l=s

    def reverse_list(self):
        try:
            lg.info('1st program began here')
            d=self.l[::-1]
            lg.info('Done successfully')
            return d
        except Exception as e:
            lg.info('there is error in your first program',e)


    def access(self,a):    # 2. try to access 234 out of this list
        try:
            lg.info('2nd program begins')
            p=a[7][0]
            lg.info('Done successfully')
            return p
            lg.info('program run successfully')

        except:
            lg.info('something when wrong')


    def access1(self,m):     # 3 . try to access 456
        try:
            lg.info('3rd program begins')
            l=m[5][1]
            lg.info('program done successfully')
            return l
        except Exception as e:
            lg.error('not found')


    def extract_only_list(self,m):    # 4 . Try to extract only a list collection form list l
        lg.info('4rd program begans here')
        try:
            l2 = []
            for i in m:
                if type(i)==list:
                    l2.append(i)
            lg.info('done successfully')
            return l2

        except:
            lg.info('something went wrong')


    def ex_sudh(self,a):  # 5 . Try to extract "sudh"
        try:
            lg.info('5th program begins')
            for i in a:
                if type(i)==dict:
                    if 'sudh' in i.values():
                        print('found')
            lg.info('Done successfully')
        except:
            lg.info('something wrong')


    def key_dic(self,a):
        lg.info('2nd last program began')
        l2=[]
        try:
            for i in a:
                if type(i)==dict:
                    for k,v in i.items():
                        l2.append(k)
            lg.info('done successfully')
            return l2
        except:
            lg.info('something when wrong')


    def value_dic(self,a):
        lg.info('last program began')
        l2=[]
        try:
            for i in a:
                if type(i)==dict:
                    for k,v in i.items():
                        l2.append(v)
            lg.info('Done successfully')
            return l2
        except:
            lg.info('something when wrong')

    lg.shutdown()





obj=list_le(l)
print(obj.reverse_list())
print(obj.access(l))
print(obj.access1(l))
print(obj.extract_only_list(l))
print(obj.ex_sudh(l))
print(obj.key_dic(l))
print(obj.value_dic(l))
































