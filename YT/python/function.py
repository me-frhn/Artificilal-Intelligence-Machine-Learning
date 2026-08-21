def add(x , y):
    return x + y

print("the sum of 5 and 6 is",add(5,6))

def sub(a,b):
    return a - b

print("the difference between 5 and 6 is ",sub(5,6))

def greet():
    print("Hello!")
    print("Hello Again!")
    pass
greet()

def check_weather(temperature):
    if temperature > 25:
        print("It's hot")
    else:
        print("It's not hot")
temp = int(input("enter the temperature:"))
check_weather(temp)

def return_f_and_l():
    numbers = [1,2,3,4,5]
    fnum = numbers[0]
    lnum = numbers[-1]
    return fnum,lnum

f,l = return_f_and_l()
print(f"first = {f} , last = {l}")