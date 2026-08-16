# there are some reserved words (keywords) which we cant use as a identifier
#This is used for single lined comment
#the multi lined comment is used for documentation purpose of multiplr lines


''' This is a multi line comments


'''
tot_price = 100 #Snake_case (prefer snake_case for )
finPrice = 100 #camelCase
FinPrice = 100 #PascalCase

#Program to add two number
a=5
b=10
sum=a+b
print(sum)

#Operators
''' there are 4 types of operators i.e
    Arithmatic
    Relations/Comparison
    Assignment
    Logical
'''
#Arithmatic Operators
x=10
y=2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)

#Relational operators >,<,<=,>=,==,!=
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)
print(x==y)
print(x!=y)


#Assigment Operators =,+=,-=,/=,*=
a+=x

#logical Operators not , and , or
var = False
print(not(var))

print((5>3) and (2<0))
print((5>3) or (2<0))

#operator precedence
'''

()
**
*,/,%
+,-
==,!=,>,>=,<,<=
not
and
or

if any expression have both operators we go from left to right
'''
