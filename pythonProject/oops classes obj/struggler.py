# a='vghgf h'
s='hii jbbj'
import logging as lg

lg.basicConfig(filename='struggler', level=lg.INFO, format='%(asctime)s,%(message)s')


class string_:


    def __init__(self,a):
         self.s = a


    def first1(self,b):  # 1 . Try to extract data from index one to index 300 with a jump of 3
         # self.s = a
         try:
            lg.info('ready to start')
            r = b[1:30]
            return r
            lg.info('Done successfully')
         except:
            lg.error('check the slicing sequence')
            print('there is issue')


program=string_(s)
print(program.first1('hvag'))