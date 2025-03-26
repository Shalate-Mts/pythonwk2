#Create an empty list
my_list = []

#append 10,20,30,40 to list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Insert 15 in the 2nd postion
my_list.insert(1, 15)

#Create a new list and and add to my_list
new_list = [50, 60, 70]
my_list.extend(new_list)

#Remove the last element of list
my_list.pop()

#sort the list in ascending
my_list.sort()

#Find and print index of value 30
index = my_list.index(30)
print('my index is', index)