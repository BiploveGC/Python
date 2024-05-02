print('line 1',end=', ')
print('line 2')
s='abcdefg'
print(id(s))
print(len(s))
s2=s[1:3]
print(s2)
s2=s[-1:-3:-1]+s[0:2]
print(s2)

myList=[0, 1, 2, 3, 4, 'hello']
var1=myList[0]
var2=myList[1]
var3=myList[2]
var4=myList[3]
var5=myList[4]

print(var1)
print(type(var1))

print(var4)
print(type(var4))

print(var5)
print(type(var5))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters[2:5]=['C', 'D', 'E']
print(letters)

list1=['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']

list1[2][1][2].append('h')
list1[2][1][2].append('i')
list1[2][1][2].append('j')

print(list1)

a, b=0, 1
while(a<10) :
    print(a)
    a,b=b, a+b

myList=['a','b','c','d','e','f']
myList.reverse()
print(myList)
