#1. What exactly is []?
Ans: [] it is symbot to represent list in python language. [] this is a empty list. list can sotre hetrogenious values.

#2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
Ans: spam =[2,4,6,8,10]
#To assign third value as hello in the list named spam we use spam.insert(2,'hello') it will assign hello at 3rd position
spam.insert(2,'hello')
spam

#3. What is the value of spam[int(int(&#39;3&#39; * 2) / 11)]?
spam[int(int('3' * 2) / 11)]
4. What is the value of spam[-1]?
Ans:d

5. What is the value of spam[:2]?
Ans:['a', 'b']


#6. What is the value of bacon.index('cat')? bacon = [3.14, 'cat', 11, 'cat', True]
//bacon.index('cat') will select the first available element in the list, that is at index 1//
Ans: bacon.index('cat') is 1

7. How does bacon.append(99) change the look of the list value in bacon?
Ans: [3.14, 'cat', 11, 'cat', True, 99]

#8. How does bacon.remove('cat') change the look of the list in bacon?
bacon.remove('cat') remove method removes the elements based on value and value present will be removed and remaing list will be present
Ans: [3.14, 11, 'cat', True, 99]

#9. What are the list concatenation and list replication operators?9. What are the list concatenation and list replication operators?
list concatenation is like addintion of the two list and replication is like copy side by side list/string.

k = bacon +spam
k
Ans: [3.14, 11, 'cat', True, 99, 'a', 'b', 'c', 'd']
n = bacon*2
n
Ans: [3.14, 11, 'cat', True, 99, 3.14, 11, 'cat', True, 99]

10. What is difference between the list methods append() and insert()?
append(x) methodused to add elements given elements in list at the end

insert(i,x) i is index and x is value kept at specified index.

bacon.append('e')
bacon
Ans: [3.14, 11, 'cat', True, 99, 'e']
bacon.insert(3,False)
bacon
Ans: [3.14, 11, 'cat', False, True, 99, 'e']


11. What are the two methods for removing items from a list?
Ans:remove() this method will remove element based on value.
pop() method will remove element at the end/ specified index retuns the element which is removed
bacon
[3.14, 11, 'cat', True, 99]
bacon.remove(True)
bacon
[3.14, 11, 'cat', 99]
bacon
[3.14, 11, 'cat', 99]
bacon.pop()
99
Bacon
[3.14, 11, 'cat']
bacon.pop(2)
'cat'
bacon
[3.14, 11]


#12. Describe how list values and string values are identical.
Ans: Both strings and lists have lengths: a string's length is the number of characters in the string; a list's length is the number of items in the list.
Each character in a string as well as each item in a list has a position, also called an index but string are immutable, list are mutuable

#13. What's the difference between tuples and lists?
tuple is immutable data type, data present in the tuple cannot be reassigned or manupulated.

list is mutable data type, data present in the list can be reassigned and manupulated.

# 14. How do you type a tuple value that only contains the integer 42?
Ans:(42,) (The trailing comma is mandatory. otherwise its considered as a int by python Interpreter)
k=(42,0)
type(k)
tuple


15. How do you get a list value's tuple form? How do you get a tuple value's list form?
t =(1,8,9,10,0,8,6,5,43)
# tuple to list form
l = list(t)
l
[1, 8, 9, 10, 0, 8, 6, 5, 43]
# list to tuple form
t = tuple(l)
t
(1, 8, 9, 10, 0, 8, 6, 5, 43)
#16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
Ans: The list value itself contains other values. The value [] is an empty list that contains no values, similar to '' , the empty string.

17. How do you distinguish between copy.copy() and copy.deepcopy()?
Ans: copy.copy() will copy the object reference of value to anohter variable, any changes in the reference will have chage in origintal object

copy.deepcopy() will copy object in seperate location and changes to copy variable will not be any effect on original object