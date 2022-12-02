#example 1:

#common way
s1=[1,2,3,4,2,3,4,5,7]
s2=set()
for i in s1:
    if i%2!=0:
        s2.add(i)
print(s2)

#output :{1,3,5}

# with comprehention:
s3={i for i in s1 if i%2!=0}
print(s3)