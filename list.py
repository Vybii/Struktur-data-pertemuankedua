buah = ["apple", "banana", "cherry", "apple", "cherry"]
print(buah)

buah = ["apple", "banana", "cherry"]
print(len(buah))

liststr = ["dragonfruit", "banana", "cherry"]
listint = [1, 5, 0, 3, 5, 8]
listbool = [True, False, False, True]

listaslinya = ["bisa", 34, True, 40, "nampung", "banyak", "tipe", "data"]

buah = list(("apple", "banana", "cherry"))
print(buah)

#Access list
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi"]
print(thislist[2:4])

thislist = ["apple", "banana", "cherry", "melon", "mango"]
print(thislist[-3:-1])

#change list
listubah = ["apple", "banana", "cherry"]
listubah[1:2] = ["blackcurrant", "watermelon"]
print(listubah)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#add list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#remove list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#loop list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#sort list
thislist = ["orange", "mango", "kiwi", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)