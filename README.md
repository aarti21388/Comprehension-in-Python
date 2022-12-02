# What are comprehentions in python? Why do we use them?
## Diffrence between list , dict ,set & generator comprehentions

-> Comprehentions in python provide us with a short and  concise way to construct new sequences(such as lists,set,dictionary etc.) using sequences which have been already defined.
-> We can create new sequences using a given python sequence.
-> This is called comprehention.

## Python supports the following 4 types of comprehentions:

* List comprehentions
* Dictionary comprehentions
* Set comprehentions
* Generator comprehentions

## List Comprehention [It will generate new list]
## Syntax : [expression for item in iterable if condition]

    ls=[i*i for i in range(6) if i%2 != 0]
    print(ls)

    Output:[1,9,25]



![Screenshot_20221202_112242_YouTube](https://user-images.githubusercontent.com/116127790/205371547-cb57a10d-69e2-4ae4-a163-20ef3e9794af.jpg)
