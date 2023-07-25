# 1
"""
l = []
for i in range(2000, 2501):
    if i%5 == 0 and i%8 == 0:
        l.append(i)
print(l)
"""
"""
# 2
a = int(input("enter number"))
for i in range(1,11):
    print(f"{i}x{a} = ", (i*a))
"""
"""
# 3
l = [9,8,7,6,5,4,3,2,1]
l.sort()
print(l[0])
"""
"""
# 4
l = [1,2,3,4,5,6,7,8,9]
l.sort()
l.pop(-1)
print(l[-1])
"""

# 5
"""
l = [1,2,3,4,5,6,7,8,9,10]
l1 = []
l2 = []
for i in l:
    if i%2 == 0:
        l2.append(i)
    else:
        l1.append(i)
print(l1)
print(l2)
"""
# 6
"""
i = [1,2,3,4,5,6,7,8,9]
print(i[::-1])

"""
# 7
"""
for i in range(0,51):
    if i%2 != 0:
        print(i)
"""

# 8
"""
l = [1,2,3,4,5,6,7,8,9,10,11,13]
c1 = 0
c2 = 0
for i in l:
    if i%2 == 0:
        c2 += 1
    else:
        c1 += 1
print("no of odd numbers-", c1)
print("no of even numbers-", c2)
"""

# 9
"""
import re
a = '216.08.094.196'
m = a.replace('0', '')

print(m)

"""
# 10
"""
import re
m = "ants antelopes bee bird animal cat amoeba"
x = re.findall("a+[a-z]+s", m)
print(x)
"""

# 11
"""
import re
g = "they ate 6 apples and 10 banana"

g = g.replace('6', 'six')
g = g.replace('10','ten')
print(g)
"""
# 12
"""
a = int(input("enter age"))
if a == 18 or a > 18:
    print("eligible for voting")
else:
    print("Not eligible for voting")
"""

# 13
"""
a = int(input("enter no of units"))
if a == 100 or a< 100:
    print("No charge")
elif a > 100 and a < 201:
    b = a-100
    print("price is", b*5)
elif a > 200:
    b = a-200
    c = b*10 + 100*5
    print("price is", c)
"""

# 14
"""
a = int(input("enter percentage"))
if a> 90:
    print("A")
elif a>80 and a < 91:
    print("B")
elif a> 59 and a< 81:
    print("C")
else:
    print("D")
"""


