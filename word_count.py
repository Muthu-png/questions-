
def word():
 string = str(input(".... :"))
 list_f = []
 for i in range(0,len(string)):
    count =0
    for j in range(-1,len(string)):
        if (i == j):
            count+=1
            x= list_f.append(string[i]) 
            m=set(list_f)
                
            print(m)    
word()         

               



