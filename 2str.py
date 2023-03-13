input1 = input("enter the str1 : ")
input2 = input("enter the str2 : ")
if (len(input1) > len(input2)):
   largeStr = input1
   smallStr = input2
else:
    largeStr = input2   
    smallStr = input1   
row =0
col =len(largeStr) 
for k in range(0,len(largeStr)):
    reverse = largeStr[::-1]
print(" "+smallStr)
for i in range(0,3):
    for j in range(len(largeStr)+1):
        if i == j:
            print(largeStr[j],end="")
        elif i==row and j==col:
             print(reverse[i],end="")
             row=row+1
             col=col-1
            #  sliceStr=input1[4:5:1] 
        else:
            print(end=" ")
    print("")    