vowel = 'aeiouAEIOU'

word = str(input('enter your word!   '))
count = 0
for i in word:
    if i in vowel:
        count +=1
print(count)

