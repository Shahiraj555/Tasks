# 1 . Try to extract data from index one to index 300 with a jump of 3
# 2. Try to reverse a string without using reverse function
# 3. Try to split a string after conversion of entire string in uppercase
# 4. try to convert the whole string into lower case
# 5 . Try to capitalize the whole string
# 6 . Write a diference between isalnum() and isalpha()
# 7. Try to give an example of expand tab
# 8 . Give an example of strip , lstrip and rstrip
# 9.  Replace a string charecter by another charector by taking your own example
# "sudhanshu"
# 10 . Try  to give a defination of string center function with and exmple
# 11 . Write your own definition of compiler and interpretor without copy paste form internet in your own language
# 12 . Python is a interpreted of compiled language give a clear ans with your understanding
# 13 . Try to write a usecase of python with your understanding .


s = "this is My First Python programming class and i am learNING python strings and its function"
import logging as lg

lg.basicConfig(filename='string.loe', level=lg.INFO, format='%(asctime)s,%(message)s')


class string_:



    def __init__(self,a):
         self.s = a


    def first1(self,a): # 1 . Try to extract data from index one to index 300 with a jump of 3
        # self.s = a


        try:
            lg.info('ready to start 1st program')
            r = s[1:30:3]
            print(r)
            lg.info('Done successfully')
        except:
            lg.error('check the slicing sequence')
            print('there is issue')




    def second(self, b):    # 2. Try to reverse a string without using reverse function
        # self.s = b
        lg.info('second program starts')
        try:
            t = self.s[::-1]
            print(t)
            lg.info('done successfully')
        except:
            lg.error('their is error')



    def third(self,y):        # 3. Try to split a string after conversion of entire string in uppercase
        try:
            lg.info('Third code starts here')
            l=s.upper().split()
            print(l)
            lg.info('printed successfully')
        except Exception as e:
            lg.error('there is a error in third code',e)




    def four(self,a):
        self.a=a          # 4. try to convert the whole string into lower case
        try:
            lg.info('fourth codes begin')
            l=self.a.lower()
            print(l)
            lg.info('code successfully run')
        except:
            lg.error('Something is wrong')



    def five(self,a):     # 5 . Try to capitalize the whole string
        try:
            lg.info('fiveth program begin')
            l=s.capitalize()
            print(l)
            lg.info('proram 5 done')
        except:
            lg.error('there is an issue')



    def six(self):
        try:
            lg.info('prograam six begin')
            if self.s.isalnum():
                print('its numeric and alphabetic')

            else:
                print('it is alphabetic')
            lg.info('Done sucessfully ')

        except Exception as e:
            lg.info('check your string once',e)


    def seven(self):
        try:
            lg.info('program seven begin')
            a=self.s.replace('python', 'classes').replace('Python','C++')
            lg.info('Done sucessfully ')
            return a

        except:
            lg.error('something when wrrong')



lg.shutdown()





program1=string_(s)
# print(program1.first1(s))
# print(program1.second(s))
# print(program1.third(s))
# print(program1.four(s))
# print(program1.five(s))
# print(program1.six())
# print(program1.seven())














