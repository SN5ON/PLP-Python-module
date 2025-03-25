#create an empty list
my_list = []
#append list with elements 10,20,30,40
my_list.append('10, 20, 30, 40')
#insert the value 15 at the second position
my_list.insert(2, '15')
#extend list with another list[50,60,70]
my_list1 = [50, 60, 70]
my_list.extend(my_list1)
#remove the last element from my_list
del my_list[-1]
#sort list in ascending order
my_list = [10, 30, 50, 20, 40, 60]
my_list.sort()
#find and print the index of the value 30 in my_list
my_list = [10, 20, 30, 40, 50, 60]
my_list.index(30)
print(my_list.index(30))