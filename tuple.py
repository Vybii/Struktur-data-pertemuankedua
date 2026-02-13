#unchangeaable
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#tuple access
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#update tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#unpack tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#loop tuple 
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

#join tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)