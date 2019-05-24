
#################################
## 1. Functional Programming
#################################

# WE CAN SUPPLY INLINE TYPE HINTS:
from typing import Optional

values: List[int] = []
best_so_far: Optional[float] = None

# The typing module contains many other types, only a few of which we’ll ever use:

# the type annotations in this snippet are all unnecessary
from typing import Dict, Iterable, Tuple
# keys are strings, values are ints
counts: Dict[str, int] = {'data': 1, 'science': 2}
# lists and generators are both iterable
if lazy:
evens: Iterable[int] = (x for x in range(10) if x % 2 == 0)
else:
evens = [0, 2, 4, 6, 8]
# tuples specify a type for each element
triple: Tuple[int, float, int] = (10, 2.3, 5)

##################################
# 1.1=zip and Argument Unpacking
##################################

# Uzing zip in order to itera over various iterables together(in parallel)
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
# zip is lazy, so you have to do something like the following
creating_pair = [pair for pair in zip(list1, list2)]    # is [('a', 1), ('b', 2), ('c', 3)]
print(creating_pair)

# NEW: Also, we can use * to unzip a iterables as shown below:
pairs = [("a",1),("b",2),("c",3)]
letters, numbers = zip(*pairs)
print(letters,numbers)

########################
# 1.2=args and kwargs
########################

# Note: Higher-order function : Takes as input some function f and returns a new
# function that for any input returns twice the value of f:
def doubler(f):
    # Here we define a new function that keeps a reference to f
    def g(x):
        return 2 * f(x)

    # And return that new function
    return(g)

def f1(x):
    return(x+1)

g = doubler(f1)
assert g(3) == 8, "(3+1) * 2 should equal 8"
assert g(-1) == 0, "(-1+1) * 2 should equal 0"

########################
# 1.3=Type Annotations
########################
## 1.3.1= How to write Type Annotations
# Option 1
def total(xs: list) -> float:
    return(sum(total))

# Option 2
from typing import List
def total(xs: List[float]) -> float:
    return(sum(total))

# Note:
## Types are an important form of documentation.

# Option 1: Most Pythonic ways
def dot_product(x:Vector, y:Vector) -> float:

# Option 2: Good way but not the best
def dot_product(x,y): ...

# Usin mypy, that will read your code, inspect annotations, let you know errors
# before you ever run your code

# Example of error:

#################################
# 2. Regular Expressions
#################################
# SUPER IMPORTANT: => re.match checks whether the beginning of a string matches a regular expression
#                  => while re.search checks whether any part of a string matches a regular expression

import re

re_examples = [                        # All of these are True, because
not re.match("a", "cat"),              #  'cat' doesn't start with 'a'
re.search("a", "cat"),                 #  'cat' has an 'a' in it
not re.search("c", "dog"),             #  'dog' doesn't have a 'c' in it.
3 == len(re.split("[ab]", "carbs")),   #  Split on a or b to ['c','r','s'].
"R-D-" == re.sub("[0-9]", "-", "R2D2") #  Replace digits with dashes.
]
assert all(re_examples), "all the regex examples should be True"

#################################
#  3. Randomness
#################################
# Because often in Data Science we need random numbers, it is important to use
# the random module
import random
random.seed(10)
four_uniform_randoms = [random.random() for _ in range(4)] # Here we use _ to create a list with
# [0.5714025946899135,       # random.random() produces numbers
#  0.4288890546751146,       # uniformly between 0 and 1.
#  0.5780913011344704,       # It's the random function we'll use
#  0.20609823213950174]      # most often.
print(four_uniform_randoms)

# SUPER IMPORTANT: random module actually produces pseudorandom (deterministic) natural_numbers
# based on internal state, and you can use random.seed in order to have reproducible results:

# Using random.randrange, which takes either one or two arguments and returns and element chosen
# randomly from the corresponding range:
rand1 = random.randrange(10)    # choose randomly from range(10) = [0, 1, ..., 9]
rand2 = random.randrange(3, 6)  # choose randomly from range(3, 6) = [3, 4, 5]
print(rand2)

# Using random.shuffle
up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)
print(up_to_ten)
# [7, 2, 6, 8, 9, 4, 10, 1, 3, 5]   (your results will probably be different)

# Using random.choice
my_best_friend = random.choice(["Alice", "Bob", "Charlie"])     # "Bob" for me
# Using random.sample
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)  # [16, 36, 10, 6, 25, 9

# To choose a sample of elements with replacement (i.e.; allowing duplicate), you can make
# multiple calls to random.choice
four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacement)
#################################
# 4. Iterables and Generators
#################################
# Using generators when we need to iterate over a collection using for and in
# Way 1: Using yield operator
def generate_range(n):
    i = 0
    while i < n:
        yield i
        i+=1
# In the following loop will consume the yielded values one at a time until none
# are left
for i in generate_range(100):
    print(i)

## With a generator, you can create an infinite sequence:
def natural_numbers():
    """Returns 1,2,3,..."""
    n = 1
    while True:
        yield n
        n += 1
# for i in natural_numbers():
#     if(i==100):
#         break
#     else:
#         print(i)

## Generator comprehension

# Example1: With for wrapped in parentheses
#evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)

# Example2: With for wrapped in parentheses
data = natural_numbers()
evens = (x for x in data if x % 2 == 0)
evens_squares = (x ** 2 for x in evens)
evens_square_ending_in_six = (x for x in evens_squares if x % 10 == 6)

for i in evens_square_ending_in_six:
    if(i > 10000):
        break
    else:
        print(i)

# Example 3: In lists and generators, we are going to need values and indices,
# therefore it is possible that we are going to need enumerate function
names = ["Alice", "Bob", "Charlie", "Debbie"]

# Pythonic way
for i,name in enumerate(names):
    print(i,name) # enumerate returns pairs(index,value)

#################################
# 5. Object-Oriented Programming
#################################

# Recomendation of using Subclasse that inherit funcitonality from paren class

# Example: Using a non-reset-able clikcer
# A subclass inherits all the behavior of its parent class.
class NoResetClicker(): #Here it is entering an object of the parent class
    # This class has all the same methods as CountingClicker
    # Class constructor is like the following:
    def __init__(self,count=0):
        self.count = count

    def click(self, num_times=1):
        """Click the clicker some number of times"""
        self.count += num_times

    def read(self):
        """Read method that returns the count of the clicker"""
        return self.count

    # Except that is has a reset method that doss nothing.
    def reset(self):
        pass

# Using NoResetClicker
clicker4 = NoResetClicker()
assert clicker4.read() == 0

# To define Classes in python we use clas keyword and PascalCase name:
class CountingClicker:
    """A class can/should have a docstring, just like a function"""

    # Note: Class methods whose names start with an underscore are- by convention-
    # considerted "private", and users of the class are not supposed to directly
    # call them. However, Python will not stop users from calling them

    # Class constructor is like the following:
    def __init__(self,count=0):
        self.count = count

    def click(self, num_times=1):
        """Click the clicker some number of times"""
        self.count += num_times

    def read(self):
        """Read method that returns the count of the clicker"""
        return self.count

    def reset(self):
        """Reset function that is a void (Java), It does not return anything
            and put in zero the clikcer"""
        self.count = 0

    # def __rep__(self):
    #     """This method allows to produce a string representation of a class instance"""
    #     return f"CountingClicker(count={self.count})"  # f"" working in >= 3.6)

# Applying assert in class clicker1
clicker = CountingClicker()
assert clicker.read() == 0, "Clicker should start with count 0"
clicker.click()
clicker.click()

assert clicker.read() == 2, "After two clicks, clicker should have count 2"
clicker.reset()
assert clicker.read() == 0, "After restet, clicker should be back to 0"

# Creating instances of the class & Using internal methods
clicker1 = CountingClicker() # Initializing to 0
print(clicker1.read())
clicker3 = CountingClicker(count=100) # This is the most pythonic way of doing it
clicker3.click()
clicker3.click()
print(clicker3.read())

#################################
# 6. Automated Testing and Assert
#################################

# How can we be confident our code is correct ?
# Part 1: Doing it with types
# Part 2: Doing it with automated tests

# Example 1: Testing a function
def smallest_item(xs):
    return(min(xs))

list1 = [10,20,5,40]
assert smallest_item(list1) == 5, "It should be given 5, and it is working"

# Example 2: Assert things about inputs to functions
def smallest_item(xs):
    assert xs, "Empty list has no smallest item"
    return min(xs)
