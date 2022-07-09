# q3 : Try to extract all the list entity
# q4 : Try to extract all the dict enteties
# q5 : Try to extract all the tuples entities
# q6 : Try to extract all the numerical data it may b a part of dict key and values
# q7 : Try to give summation of all the numeric data
# q8 : Try to filter out all the odd values out all numeric data which is a part of a list
# q9 : Try to extract "ineruon" out of this data
# q10 :Try to find out a number of occurances of all the data
# q11 : Try to find out number of keys in dict element
# q12 : Try to filter out all the string data
# q13 : Try to Find  out alphanum in data
# q14 : Try to find out multiplication of all numeric value in  the individual collection inside dataset
# q15 : Try to unwrape all the collection inside collection and create a flat list

l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":"kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]
import logging as lg
lg.basicConfig(filename="chgl", level=lg.DEBUG, format="%(asctime)s %(message)s")
class challenge:
  def __init__(self,a):
    self.s=a

  def extr(self,m):   #Try to extract all the list entity
    l2=[]
    lg.info(' 1st program begins')
    try:

      for i in m:
        if type(i)==list:
          l2.append(i)
        else:
          pass
      return l2
    except:
      lg.info('there is no list')


  def find_dict(self,m):     # q4 : Try to extract all the dict enteties
    lg.info('2nd program begins')
    l2=[]

    try:
      for i in m:
        if type(i)==dict:
          l2.append(i)
          lg.info('program run successfully')
      return l2
    except:
           lg.info('dictionary is not there')


  def find_tuple(self,k):   # q5 : Try to extract all the tuples entities
    lg.info('3rd program begins')
    l2 = []
    try:
      for i in k:
        if type(i) == tuple:
          l2.append(i)
          lg.info('program run successfully')
      return l2
    except:
      lg.info('tuple is not there')


  def all_num_extract(self,a):  # q6 : Try to extract all the numerical data it may b a part of dict key and values
    lg.info('4rd program begins')
    l2=[]
    try:
      for i in a:
        if type(i)==list or type(i)==tuple or type(i)==set:
          for k in i :
            if type(k)==int:
              l2.append(k)
        if type(i)==dict:
          for c,v in i.items():
            if type(c)==int or type(v)==int:
               l2.append(c)
               l2.append(v)

      return l2

    except:
      lg.info('there is no values')


  def sum_values(self,a):  # q7 : Try to give summation of all the numeric data
    lg.info('5th program begins')
    l2=[]
    try:
      for i in a:
        if type(i)==list or type(i)==tuple or type(i)==set:
          for k in i :
            if type(k)==int:
              l2.append(k)
        if type(i)==dict:
          for c,v in i.items():
            if type(c)==int or type(v)==int:
               l2.append(c)
               l2.append(v)
            lg.info(sum(l2))


    except:
      lg.info('there is no values')


  def filter_odd(self,a):    # q8 : Try to filter out all the odd values out all numeric data which is a part of a list
    lg.info('6th program begins')
    l2=[]
    l3=[]
    try:
      for i in a:
        if type(i)==list or type(i)==tuple or type(i)==set:
          for k in i :
            if type(k)==int:
              l2.append(k)
        if type(i)==dict:
          for c,v in i.items():
            if type(c)==int or type(v)==int:
               l2.append(c)
               l2.append(v)
      print(l2)
      for w in l2:
        if (w / 2 != 0):
           l3.append(w)
      lg.info(l3)

    except:
      lg.info('their something error ')

  def extract_ineuron(self,a):  # q9 : Try to extract "ineruon" out of this data
    l2=[]
    try:
      lg.info('7th program begins')
      for i in a:
        if type(i)==list or type(i)==tuple or type(i)==set:
          for k in i:
            if k=='ineuron':
              l2.append(k)
        if type(i)==dict:
          for k,v in i.items():
            if k=='ineuron' or v=='ineuron':
              l2.append(v)
      lg.info(l2)
    except Exception as e:
      lg.info(e)

  def number_of_occurence(self):   # q10 :Try to find out a number of occurances of all the data
    l1 = []
    lg.info('8th program begins')
    try:
      for i in self.s:
        if type(i) == list or type(i) == tuple or type(i) == set:
          for j in i:
            l1.append(j)
        if type(i) == dict:
          for k, v in i.items():
            l1.append(k)
            l1.append(v)

      for s in set(l1):
        lg.info(f'{s} --  {l1.count(s)}')

    except Exception as e:
      lg.exception(e)


  def no_keys(self):
    try:
      l1=[]
      lg.info('9th program begins')
      for i in self.s:
        if type(i)==dict:
          for k,v in i.items():
            l1.append(k)
            lg.info(f'{k} -- {l1.count(k)}')
    except:
      lg.info('their is some error')

  def extract_string(self):            # q12 : Try to filter out all the string data
    lg.info('10th program begins here')
    l1=[]
    try:
      for i in self.s:
        if type(i)==list or type(i)==tuple or type(i)==set:
          for j in i:
            if type(j)==str:
              l1.append(j)
        if type(i)==dict:
          for k,v in i.items():
            if type(k)==str or type(v)==str:
              l1.append(k)
              l1.append(v)

      lg.info(l1)
    except:
      lg.info('their is a error')

  def find_alphanumeric(self): # q13 : Try to Find  out alphanum in data
    l1 = []
    lg.info('11th program begins')
    try:
      for i in self.s:
        if type(i) == dict:
          for k, v in i.items():
            if type(k) == str:
              if k.isalnum():
                l1.append(k)
      lg.info(l1)
    except Exception as e:
      lg.exception(e)

  def mul(self):      # q14 : Try to find out multiplication of all numeric value in  the individual collection inside dataset
    lg.info('12th program begins')
    l2=[]
    try:
      for i in self.s:
        if type(i) == list or type(i) == tuple or type(i) == set:
          for k in i:
            if type(k) == int:
              l2.append(k)
        if type(i) == dict:
          for c, v in i.items():
            if type(c) == int or type(v) == int:
              l2.append(c)
              l2.append(v)

      result = 1

      for i in l2:
        result*=i
      lg.info('Done successfully')
      return result
    except:
      lg.info('something wrong')
















obj=challenge(l)
# print(obj.extr(l))
# print(obj.find_dict(l))
# print(obj.find_tuple(l))
# print(obj.all_num_extract(l))
# print(obj.sum_values(l))
# print(obj.filter_odd(l))
# print(obj.extract_ineuron(l))
# print(obj.number_of_occurence())
# print(obj.no_keys())
# print(obj.extract_string())
# print(obj.find_alphanumeric())
# print(obj.mul())




