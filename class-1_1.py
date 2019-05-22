############################################################
# Control Flow & Truthiness & Sorting & List Comprehensions
############################################################

########################
## List Comprehensions
########################


##################
## Sorting
##################


##################
## Truthiness
##################

# Python uses the value None to indicate a nonexisten value. Similar to other
# languages's null
x = None


# Booleans in python are Capitalized
true_equals_false = True == False
print(true_equals_false)



##################
## Control Flow
##################
#You can also write a ternary if-then-else on one line, which we will do occasionally:
parity = "even" if x % 2 == 0 else "odd"

#Python has a while loop:
x = 0
while x < 10:
    #print(f"{x} is less than 10")
    print(str(x) + " is less than 10")
    x += 1

#although more often we’ll use for and in: # range(10) is the numbers 0, 1, ..., 9
for x in range(10):
    print(f"{x} is less than 10") # Python >= 3.6

#If you need more complex logic, you can use continue and break:
for x in range(10):
    if x == 3:
        continue  # go immediately to the next iteration
    if x == 5:
        break     # quit the loop entirely
    print(x)
#This will print 0, 1, 2, and 4.

###################################
# Dictionaries & Counter & Sets
##################################
# Counter and Sets
# Note: A counter turns a sequence of values into a defaultdict (int)-like
# object mapping keys to counts:
from collections import Counter
c = Counter([0,1,2,0])
print(c)
c.most_commom(1)

# Counter has most_commom method
for number,count in c.most_commom(1):
    print(number,count)

# Sets; Collection of distinct elements
# for empty set, we have to use set()
s = set()
s.add(1)
s.add(2)
s.add(2)

for i in range(1,100):
    s.add(i)
print(s)

# Sets are used for two reasons:
# 1. For a faster in operation  for a membership Testing
stop_number_list = ["a","an","at"] + list(s) + ["yet","you"]
## finding in list
print("zip" in stop_number_list)
#findin in Sets
stop_number_set = set(stop_number_list) # This is faster
print("zip" in stop_number_set)

# 2. To find the distinct items in a collection
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)                # 6
item_set = set(item_list)                 # {1, 2, 3}
num_distinct_items = len(item_set)        # 3
distinct_item_list = list(item_set)       # [1, 2, 3]
print(distinct_item_list)

# Pythonic way of dict
empty_dict = {}

# KeyError
grades = {"Joel": 80, "Tim": 95}
try:
    kates_grad = grades["Kate"]
except KeyError:
    print("No grade for that key")

# Existence of key using in operator
joel_has_grade = "Joel" in grades
print(joel_has_grade)

# get method, other way to look for keys and notes
kates_grade = grades.get("Kate",0)
print("it gives zero because there is no key Kate in grades with get method", kates_grade)

# Different way to look up keys
tweet = {
"user" : "joelgrus",
"text" : "Data Science is Awesome",
"retweet_count" : 100,
"hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}
print(tweet)

tweet_keys = tweet.keys()
tweet_values  = tweet.values()
tweet_items = tweet.items()

print(tweet_keys)
print(tweet_values)
print(tweet_items)

# Evaluating with in operator
print("user" in tweet_keys) #
print( "user" in tweet) # OJO: Pythonic way of checking for keys
print("joelgrus" in tweet_values) # True (slow but the way to check)

# Note: Dictionary keys must be "hashable"; in particular, you cannot use lists as keys
# If you need a multipart key, you should use a tuple or figure out a way to turn the key
# into a String

# defaultdict
from collections import defaultdict

word_counts = defaultdict(int)
print(len(word_counts))
for word in document:
    word_counts[word] += 1

# This can be useful with list or dict in Functions
from collections import defaultdict
dd_list = defaultdict(list)
dd_list[3].append(1)
dd_list[1].append(2)

dd_dict = defaultdict(dict)
dd_dict["Joel"]["City"] = "Seattle"

# using lambda inside, for pair dict
dd_pair = defaultdict(lambda: [0,0]) # Note: These will be useful when we're
# using dictionaries to "collect" results by some key and don't want to have to
# check every time to see if the keys exists yet.
dd_pair[2][1] = 1
#dd_pair[3][2] = 1 # In this will give me an KeyError
print(dd_list)
print(dd_dict)
print(dd_pair)

#######################
# Lists & Tuples
######################
#unpack Lists
x, y1 = [1,2]
# if ValueError appeared, you can do the following
_, y2 = [1,2]
print(x,y1,y2)

# Python has an in operator
boolean_in_list1 = 1 in [1,2,3]
boolean_in_list2 = 0 in [1,2,3]

print(boolean_in_list1)
print(boolean_in_list2)

# Tuples are list's immutable cousins
def sum_and_product(x,y):
    return((x+y),(x*y))

sp = sum_and_product(2,3)
s, p = sum_and_product(5,10)

print(sp)
print(s)
print(p)

#######################
# Various
######################
# Doing loop
for i in [1,2,3,4,5]:
    print(i)
    for j in range(1,5):
        print(j)
        print(i+j)
    print(i)
print("Done looping")

# Lists, easier to read
easier_to_read_list_of_list = [ [1,2,3],
                                [4,5,6],
                                [7,8,9]]
print(easier_to_read_list_of_list)


# Shorcuts for module importing
import re as regex # for regex
my_regex = regex.compile("[0-9]+",regex.I)

# for dicts and collections
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

# Functions and lambdas; Python functions are first-class, which means that we
# can assign them to variables and pass them into functions just like any other arguments

# This is the style of funcitons
def double(x):
    """
    This is where you put an optional docstring that explains what the
    function does. For example, this function multiplies its input by 2.
    """
    return x * 2
print(double(2))

# Doing lambdas
y = lambda x: (x*2) # equals multiply by 2, use lambdas when there is a repetetive actions

# Function parameters
def my_print(message= "default message"):
    print(message)

my_print("Learning")
my_print()

# Strings
# raw Strings
not_tab_string = r"\t"
print(len(not_tab_string))
