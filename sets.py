thisset = {"apple", "banana", "cherry"}
print(thisset)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)


set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)


#access sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

#add sets
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#remove sets
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


#loop sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

#join sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)