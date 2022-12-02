## List COmprehention [It will generate new list]
## Syntax : [expression for item in iterable if condition]

#Example 1:
    
ls=[i*i for i in range(6) if i%2 != 0]
print(ls)

#    Output:[1,9,25]

#Example 2:
list1=[2,3,4]
list2=[12,13,14]

ls=[(i*j) for i in list1 for j in list2]
print(ls)

#    output:
 #   [24,26,28,36,39,42,48,52,56]

list1=[2,3,4]
list2=[12,13,14]

ls=[[i,j] for i in list1 for j in list2]
print(ls)

#output
# [[2, 12], [2, 13], [2, 14], [3, 12], [3, 13], [3, 14], [4, 12], [4, 13], [4, 14]]