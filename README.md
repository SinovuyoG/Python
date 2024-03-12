# Python-week1
Introductio To Python:

The computer stores its data in a memory and when it needs to retrieve that data it follows a pointer ,which is an address that represents the location of the file you are looking for.
So when we write and run a computer program, we are actually communicating with the memory. The program generates bits of data called variables.

Python is a widely used programming language, that can be used for web development, machine learning, etc. You can download python from any browser, then you can run the setup.
To access python you can open cmd, then you type Python in the command line then press enter. You will see 3 greater than symbols, thats where you can write a line of code.
To write python programs,you need to download text editors like Jupyter Notebook, Visual studio code, pycharm etc.
You need to write the file name with the .py extention.
In programming we also use COMMENTS, which serves as a reminder to some programmers about what a line of code does.

VARIABLES AND TYPES

A variable is a basic unit of a program. Variables stores values. 
You can add a cell on jupyter notebook by clicking outside the cell on the left margin and press "a".
You can also run a line of code in cell by pressing Shift+ Enter buttons.
A variable that starts with a number cannot be used,only variables that contain upper case,lower case and underscore are accepteble.
Traditionally in python, a variable starts with a lower case.
Variables and data types in python include:
Integers-whole numbers
floats-decimal numbers
string-collection of characters
complex numbers-used for complex mathematical calculations
Booleans- True or false values.
When working with strings, the plus operator sign is used to concatenate the strings but cannot be used to add string and numbers.its going to give an error.

DATA STRUCTURES IN PYTHON

A data structure is a way to store data.
Data structures give us the possibility to manage large amounts of data efficiently for uses such as large databases and internet indexing services.
Data structures are essential ingredients in creating fast and powerful algorithms. They help in managing and organizing data, reduce complexity, and increase efficiency.
In Python, data structures allow for the storage of a list of values in a single variable.
There is a list data structure, which stores values of any data type including a LIST within a List.
The length of a list can be determined using the length fuction.
Lists are created using square brackets:

Example:
Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.


There is a Set data structure which is similar to a list data structure but it contains only the unique elements and is declared using the curly braces.
The order of elements in a Set is not important ,unlike in a List.
There is also a Tuple data structure,which are similar to Lists, but cannot be changed once declared. They are useful when you need to store large amounts of data more effeciently i memory.
Lastly,there is a Dictionary data structure- is a collection of key-value pairs, similar to a word and its definition in a book. Dictionaries are declared using curly braces and accessed using keys.

OPERATORS
Operators are instructions that perform operations on variables and values in Python. 
They are used to manipulate and perform actions on data.
Arithmethic operators are the most commonly known as they are used for mathematical calculation.
+: Plus operator
-: Minus
*: Multiplication
**:Exponet
/: Devide returns a floating-point value, even if the result is a whole number
%: Modulus return the remainder after division
Strings can also be manipulated using operators. The addition operator can concatenate or combine two strings together, while the multiplication operator can repeat a string a certain number of times.
It's important to note that the addition operator for strings works only with two strings, while the multiplication operator can work with either a string or a number

Comparison operators, logical operators, identity operators, and membership operators are another set of operators in Python.
Comparison operators evaluate two variables or values and produce a Boolean result, either true or false. Examples include:
the double equal sign for equality(==)
less-than(<) less-than or equal to(<=)
greater than(>)
greater than or equal to(>=)

Logical operators, such as "and," "or," and "not," operate on Boolean values. 
The "and" operator returns true only if both operands are true
while the "or" operator returns true if at least one operand is true. 
The "not" operator negates the Boolean value it operates on.

Membership operators, "in" and "not in," are used to check whether a value is present in a sequence or not. For instance, using "in" can check if a number or a string exists in a given list or string.


CONTROL FLOWS

There are 3 main control flows in programming, nameley If statement, For Loop and While Loop.
The If statement allows you to execute a block of code only if a certain condition is met.
In Python, you use the if statement like this:
a = True
if a:
print ("It is true")
If the condition is true, the indented code under the if statement will be executed. 
You can add more code under the if statement by indenting it further. 
If you add an else statement, the code under that will be executed if the condition is false.
Indentation is very important in Python as it as determines the structure of your program.
A for loop is used to iterate over a list or any iterable object.
In Python, you write a for loop like this: 
for item in my_list: print item
While loop is similar to a for loop, but it keeps looping until a certain condition is false.
In Python you use a While loop like this: 
a = 0
while a < 5: 
print a, a = a + 1

It's important to make sure that the condition in the while loop will eventually become false, otherwise, the loop will continue indefinitely

FUNCTIONS

A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
In Python a function is defined using the def keyword:

Example
def my_function():
  print("Hello from a function")

The "return" keyword is used to specify the output.
Functions can take one or more arguments, and they may or may not return a value.
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
Example:
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
function may mutate a variable without returning anything. The print function is an example of a function that does not return anything, but rather prints output to the console.
The "None" keyword is used to define a null value, or no value at all.
None is not the same as 0, False, or an empty string. None is a data type of its own (NoneType) and only None can be None.
For Example:
x = None

if x:
  print("Do you think None is True?")
elif x is False:
  print ("Do you think None is False?")
else:
  print("None is not True, or False, None is just None...")

CLASSES AND OBJECTS

Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
When we define a class, we use an uppercase letter for the class name, and we start defining all the functions and attributes inside the class definition. 
To create a class, use the keyword class.
Example:
class MyClass: ##this is a class
  x = 5
p1 = MyClass()## this is an object
print(p1.x)
The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the initialization function- the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

