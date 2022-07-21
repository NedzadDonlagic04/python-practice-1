# This is a single line comment in python
# This is the print statement,it outputs the 
# passed argument to the console
print('Hello world!');

# Python is case sensitive and dynamically typed
myFirstVariable=5;

# Printing a variable in python
print(myFirstVariable);

# This is an example of a multi line statement

a = 1 + 2 + 3 \
    + 10 + 20;

print(a);

# This is another example of the same thing

a = (1 + 2 + 3
    + 10 + 20);

print(a);

"""
This is a multi line python comment
"""

# The use of ;
# From what I gathered python's philosophy or the zen of python
# says the following

"""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# TL;DR python in order to make things more readable
# and thus make the code more readable removes the usage
# of ; in certain places,for example

print('\nThis line didn\'t use a ;')
print('Neither did this one!\n')

# But you do need ; for one liners,like

print('This line did use ;');print('Because it is a one liner!')

# The fun doesn't end here tho,no more {} say hi to indentations
# I'll show this off on an IF statement

if True:
    print('\nThis is inside an if statement')

# Yep true is written as True and false as False
# And yeah the : is there instead of the usual () {}

# If you go a layer behind the indentation the statement
# executes like normal,as if it was outside the {}

if False:
    print('I will never execute!')
print('\nOutside of the indentation\n')

# while statements

counter=1
print('Countdown:')
while counter<=10:
    print(counter)
    counter+=1

# In python there is no ++ or --
# Use += or -=

print('\nCountdown:')
for x in range (0,3):
    print(x)

# In python for loops are kinda like foreach loops
# Here we say variable x starts at 0 and goes up to
# 3 (which isn't included) and if we don't specify
# it will add 1 to itself at the end of each iteration
# If we want to specify we write

print('\nCountdown:')
for x in range (0,10,3):
    print(x)

# Python doesn't have a built in do while loop
# we can emulate it as the following tho

print('\nCountdown:')
doX=0
while True:
    print(doX)
    doX+=1
    if doX>2:
        break

# One more thing before I call it a night for 
# day 1

print('\nCountdown:')
for x in range (0,10,3):
    print(x)
print(x)

# In this case the x isn't scoped to just the for loop
# it can be accessed from outside it

# Day 1 Done