l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]
#q9 : Try to extract "ineruon" out of this data

for i in l:
    if type(i)==list:
        for j in i:
            if j=='ineuron':
                print(j)

l=l[5][0]
print(l)

