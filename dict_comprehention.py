
#Exampl 1;

dict = {i:i*i for i in range(1,10)}
print(dict)

#output
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


#Example 2:

list1=[x for x in range(1,4)]
list2=['Mon','Tue','Wed']

dict1={key:value for (key,value) in zip(list1,list2)}
print(dict1)

#output 
#{1: 'Mon', 2: 'Tue', 3: 'Wed'}