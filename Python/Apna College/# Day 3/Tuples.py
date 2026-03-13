#Tuples
#tuples are the immutable sequence of values
#tuples are created by the ()

tup = (1,2,3,4,5,6,7)

#single values tuples are created only when the comma is added after the 1st element
t = (1,)
print(type(t))

print(tup)
print(type(tup))
print(tup[2])

sum = 0
for val in tup :
    sum +=val
    print(val)
print(sum)

#methods in tuple
print(tup.index(2))
print(tup.count(3))