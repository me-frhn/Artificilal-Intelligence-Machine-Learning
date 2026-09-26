# #for loops are generally used for sequestial traversal
# string = "hello"

# if 'o' in string :
#     print("o exist in hello")


# #in => membership operator
# for v in string:
#     print(v)

# for i in range (5): # range(start , stop , step)
#     print(i, "Hello world")

word = "Artificial intelligence"
ans = 0
for char in word :
    if char=='i' or char == 'a' or char == 'e' or char == 'o' or char == 'u':
        ans +=1
print("Count of vowels in word is ",ans)

