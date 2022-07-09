l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]

# q6 : Try to extract all the numerical data it may b a part of dict key and values
# l2=[]
# for i in l:
#
#
#     if type(i)==list or type(i)==tuple or type(i)==set :
#         for g in i:
#             if type(g)==int:
#                 l2.append(g)



l1=[]
for i in l:
    if type(i)==list or type(i)==tuple or type(i)==set:
        for j in i:
            if type(j)==int:
                assert isinstance(l1)
                l1=l1.append(l1)
                print(l1)