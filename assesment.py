Objects and Data Structures Assessment Test
Test your knowledge.
** Answer the following questions **

Write a brief description of all the following Object Types and Data Structures we've learned about:


.
Numbers: they represent intergers and floats in python. Integers being whole numbers and floats being decimals. They can use used to preform arithmetic.
​
Strings: any data that is wrapped around quotes. Usually words, but can be anything.
​
Lists: different or similar data types that are seperated by commas and boud together by square brackets. Contents inside of a list can be called upon through their index. Lists can be mutated and have many functions that can add or remove things in a list.
​
Tuples: are like lists but they contain only unique items, and unlike lists they are not mutatable
​
Dictionaries: are sets of data seperated by commas and held together by curly braces. Data inside comes in pairs known as key/value pairs. They key is a string while the value can be anything. Dictionaries are also unordered lists, we can reference the specific value we want by knowing the key.
​
Numbers
Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25


100*4/4+.50-.25
100.25
Answer these 3 questions without typing code. Then type code to check your answer.

What is the value of the expression 4 * (6 + 5)

What is the value of the expression 4 * 6 + 5

What is the value of the expression 4 + 6 * 5

4 + 6 * 5
34
What is the type of the result of the expression 3 + 1.5 + 4?

==> float b/c it evaluates to 8.50

What would you use to find a number’s square root, as well as its square?


1/2
# Square root: (number**(1/2))
print(4**(1/2))
​
2.0

4**2
# Square: (number**2)
print(4**2)
16
Strings
Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:


1
s = 'hello'
# Print out 'e' using indexing
print(s[1])
​
e
Reverse the string 'hello' using slicing:


-1
s ='hello'
# Reverse the string using slicing
print(s[::-1])
​
olleh
Given the string hello, give two methods of producing the letter 'o' using indexing.


4
s ='hello'
# Print out the 'o'
​
# Method 1:
print(s[4])
​
​
o

-1
# Method 2:
print(s[-1])
​
o
Lists
Build this list [0,0,0] two separate ways.


# Method 1:
my_list=[0,0,0]
print(my_list)
[0, 0, 0]

y_list2
# Method 2:
my_list2 = [0]*3
print(my_list2)
[0, 0, 0]
Reassign 'hello' in this nested list to say 'goodbye' instead:


list3
list3 = [1,2,[3,4,'hello']]
list3[2][2]='goodbye'
print(list3)
​
[1, 2, [3, 4, 'goodbye']]
Sort the list below:


ist4
list4 = [5,3,4,6,1]
list4.sort()
print(list4)
​
[1, 3, 4, 5, 6]
Dictionaries
Using keys and indexing, grab the 'hello' from the following dictionaries:


le_key
d = {'simple_key':'hello'}
# Grab 'hello'
print(d['simple_key'])
hello

k2
d = {'k1':{'k2':'hello'}}
# Grab 'hello'
print(d['k1']['k2'])
hello

0
# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
​
#Grab hello
print(d['k1'][0]['nest_key'][1][0])
hello

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
Can you sort a dictionary? Why or why not?

==> No becuase a dictionary is unordered. That is why we use keys to obtain the values from within it.

Tuples
What is the major difference between tuples and lists?

==> Tuples can not be mutated while lists can

How do you create a tuple?

==> my_tuple=('a','b') will create a new tuple.

Sets

t
What is unique about a set?<br><br> set's can only hold unique values. Meaning inside of a set, values will never repeat
Use a set to find the unique values of the list below:


list5
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))
​
​
{1, 2, 33, 4, 3, 11, 22}
Booleans
For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4.

Operator	Description	Example
==	If the values of two operands are equal, then the condition becomes true.	(a == b) is not true.
!=	If values of two operands are not equal, then condition becomes true.	(a != b) is true.
>	If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.
<	If the value of left operand is less than the value of right operand, then condition becomes true.	(a < b) is true.
>=	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	(a >= b) is not true.
<=	If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	(a <= b) is true.
What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)


F
# Answer before running cell
2 > 3
# False
False

F
# Answer before running cell
3 <= 2
# False
False

# Answer before running cell
3 == 2.0
# False
False

True
# Answer before running cell
3.0 == 3
# True
True

false
# Answer before running cell
4**0.5 != 2
# false
False
Final Question: What is the boolean output of the cell block below?


false
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
​
# True or False?
l_one[2][0] >= l_two[2]['k1']
# 3 >= 4
# false
False
