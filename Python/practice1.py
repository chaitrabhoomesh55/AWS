a = [1, 2, 3, 4, 66, 99, 36, 54,200]
f = a
print(type(a))

# list a[1:3] 2,3
print(a.remove(4))
del(a[1])
#print(a.append([5, 8, 9]))         #if u wanna add whatever is given, as a single item
print(a)
#print(a.extend([5, 8, 9]))        #it will add every element into the list
print(a)

b = a.copy()
print("b:::",b)
print(f' sorting of b is {b.sort()}')
print(f' sorting of b is {b.reverse()}')
print(b)
#print(a.copy())
def addnums():
    return 

print(f' line 22 is {addnums()}')

s = 6.7875
d = int(s)
print("line 26", type(d))

t = (6, 8, 9, 7, 8, 7)
l = list(t)
s = [t]
print(s)

import sys
print(sys.builtin_module_names)


'''

string = '  ,_closed_ ,  , 3, 88 '
string1 = 'flosed'
print(type(string))
print(string.upper())
print(string.index('s'))
print(string.replace('s', 'c'))
print(string.find('l'))
print(len(string))
new = string.rstrip()
print(new)
print(len(new))
print(f'line30 is {string.split()}')
print(f"line31 is {string.startswith(' ')}")
print(string)



tuple = ('string','string', 'car', 'dog')
tuple1 = 'string', 5,

#tuple[1]='notstring'
print(tuple + tuple1)           #('string', 'string', 5)
print(dir(tuple))
print(tuple.count('string'))
print(tuple.index('string'))



print(type(tuple))
print(type(tuple1))




lsit/tuple list

concat in 

#slicing

list: range: 

'''

#Set:

boolean_list = [6, 8, 4, 1, 9, 15]
Bool= [6, 8, 4, 1, 9, 15]

# check if all elements are true
#result = all(boolean_list > 5)
result = [True if (item < 9) else False for item in boolean_list]
print(f' line 90 {result}')
#print(f' if all the items returns True {all(result)})

if any(result):
    print("All the items in boolean_list are less than 9")
else:
    print("Not all the items in boolean_list are less than 9")

count= 0
for i in Bool:
    print(count, i)
    count = count+1

for i, item in enumerate(Bool):
    print(i, item)
    print(item)

    