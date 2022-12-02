#Example 1:

#common way

def generator(list1):
    for i in list1:
        if i %2 !=0:
            yield i

list1=[1,2,3,4,5,6,7,8,9]
gen_value=generator(list1)
print(gen_value)
print(next(gen_value))
print(next(gen_value))

#generator comprehention

gen_values = ( i for i in range(20) if i%2 !=0 )
print(gen_values)
print(next(gen_values))
print(next(gen_values))
for i in gen_values:
    print(i,end=" ")