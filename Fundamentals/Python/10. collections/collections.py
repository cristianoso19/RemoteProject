#Lists are ordered, mutable, and allow duplicate elements. They are defined using square brackets [] and can contain elements of different data types. For example:

#index:      0        1         2
fruits = ["apple", "banana", "cherry"]
print(fruits) #Output: ['apple', 'banana', 'cherry']
print(type(fruits)) #Output: <class 'list'>
print(fruits[1]) #Output: banana (accessing the second element of the list using its index)
fruits.append("orange") #This will add "orange" to the end of the list
print(fruits) #Output: ['apple', 'banana', 'cherry', 'orange

list = ["Cristian", 30, True, 3.14] #A list can contain elements of different data types
print(list) #Output: ['Cristian', 30, True, 3.14
print(type(list)) #Output: <class 'list'>

print(len(fruits)) #Output: 4 (length of the list)
print(len(list)) #Output: 4 (length of the list)

print(fruits[0:2]) #Output: ['apple', 'banana'] (accessing the first two elements of the list)
print(fruits[1:]) #Output: ['banana', 'cherry', 'orange'] (accessing the elements from index 1 to the end of the list)
if "banana" in fruits:
    print("banana is in the list") #Output: banana is in the list (checking if an element is in the list)

vehicles = ["car", "bike", "bus"]
#methods: adding elements to the list
#append() method is used to add an element to the end of the list
vehicles.append("train") #This will add "train" to the end of the list  
print(vehicles) #Output: ['car', 'bike', 'bus']
#Insert() method is used to add an element at a specific index in the list
#Insert an element at a specific index
vehicles.insert(1, "truck") #This will insert "truck" at index 1
print(vehicles) #Output: ['car', 'truck', 'bike', 'bus']

#remove() method is used to remove the first occurrence of an element from the list
vehicles.remove("bike") #This will remove "bike" from the list
print(vehicles) #Output: ['car', 'truck', 'bus']

#pop() method is used to remove an element at a specific index and return it. If no index is specified, it removes and returns the last element of the list.
removed_vehicle = vehicles.pop(1) #This will remove the element at index 1 and return it
print(removed_vehicle) #Output: truck (the removed element)
print(vehicles) #Output: ['car', 'bus'] (the list after removing the

#sort() method is used to sort the elements of the list in ascending order. If you want to sort the list in descending order, you can use the reverse parameter and set it to True.
vehicles.sort() #This will sort the list in ascending order
print(vehicles) #Output: ['bus', 'car'] (the sorted list)
vehicles.sort(reverse=True) #This will sort the list in descending order

#reverse() method is used to reverse the order of the elements in the list
vehicles.reverse() #This will reverse the order of the elements in the list
print(vehicles) #Output: ['car', 'bus'] (the reversed list)

#join lists
collection1 = ["a", "b", "c"]
collection2 = [1, 2, 3]
collection1.extend(collection2) #This will add the elements of collection2 to the end of collection1
print(collection1) #Output: ['a', 'b', 'c', 1, 2, 3] (the joined list)