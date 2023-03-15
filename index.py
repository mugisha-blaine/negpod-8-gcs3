n = int(input("Enter an integer: "))
 
# iterate from 1 to n
for i in range(1, n+1):
    # check if i is odd
    if i % 2 != 0:
        print(i, end=", ")
        
#second question

word = input("Enter a word: ").lower()

i = 0
while i < len(word):
    if word[i] not in "aeiou" and word[i] != "y":
        print(word[i], end=", ")
    i += 1
