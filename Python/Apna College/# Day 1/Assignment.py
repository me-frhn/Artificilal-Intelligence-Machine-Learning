'''


qn) Take the decimal number as input (like 45.123) and output its :
integer part:45
fractional part:.123
'''

num = input("Enter a decimal number: ")

# Split the number at the decimal point
if "." in num:
    
    integer_part, fractional_part = num.split(".")
    print("integer part:", integer_part)
    print("fractional part: ." + fractional_part)
else:
    print("integer part:", num)
    print("fractional part: .0")