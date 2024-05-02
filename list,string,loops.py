#Given a list of strings, print the number of list elements that have the same letter
# at the beginning and the end and that have length of larger 1


word=['hello', 'abba', 'cc', 'wow']
count = 0
for w in word:
    if  w[0] == w[-1] and len(w) > 1:
        count += 1
print(count)

#Output = 3
