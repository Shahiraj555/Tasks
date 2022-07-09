l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]

#try to extract 'ineuron' from dict

for i in l:
    if type(i)=='dict':
        for j in i.items():
            for k in j:
                if k=='ineuron':
                    print(k)
