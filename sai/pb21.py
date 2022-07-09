l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]

# q3 : Try to extract all the list entity
# q4 : Try to extract all the dict enteties
# q5 : Try to extract all the tuples entities
# q6 : Try to extract all the numerical data it may b a part of dict key and values
# q7 : Try to give summation of all the numeric data
# q8 : Try to filter out all the odd values out all numeric data which is a part of a list
# q9 : Try to extract "ineruon" out of this data


for i in l:
    if type(i)==list:
        print(i)