'''
The following program was written using the talk, "The Mighty Dictionary" by Brandon Craig Rhodes as a reference.
You can find the talk here: https://archive.org/details/pyvideo_276___the-mighty-dictionary-55
'''
# TEST
# d = {
#     'smtp': 21,
#     'dict': 2628,
#     'svn': 3690,
#     'ircd': 6667,
#     'zope': 9673
# }

# print(d.keys()) # Dictionary keys no longer get a 'crazy' order as mentioned in the talk (it was about Python 2.x).


# Credits for the following code snippets: https://medium.com/techtofreedom/5-uses-of-asterisks-in-python-3007911c198f

# For getting unlimited arguments [args] use "*"
def print_genius(*names):
    print(type(names))
    for n in names:
        print(n)

print_genius('Elon Mask', 'Mark Zuckerberg ', 'Yang Zhou')
# <class 'tuple'>
# Elon Mask
# Mark Zuckerberg 
# Yang Zhou


# For getting unlimited key: value pairs (keyword arguments [kwargs]), use "**"
def top_genius(**names):
    print(type(names))
    for k, v in names.items():
        print(k, v)

top_genius(Top1="Elon Mask", Top2="Mark Zuckerberg", Top3="Yang Zhou")
# <class 'dict'>
# Top1 Elon Mask
# Top2 Mark Zuckerberg
# Top3 Yang Zhou


# Restrict to Keyword-Only Arguments
def genius(*, first_name, last_name):
    print(first_name, last_name)

# genius('Yang','Zhou')
# TypeError: genius() takes 0 positional arguments but 2 were given
genius(first_name='Yang', last_name='Zhou')
# Yang Zhou


# Iterables Unpacking
A = [1, 2, 3]
B = (4, 5, 6)
C = {7, 8, 9}
L = []
for a in A:
    L.append(a)
for b in B:
    L.append(b)
for c in C:
    L.append(c)
print(L)
# [1, 2, 3, 4, 5, 6, 8, 9, 7]


# Using list comprehensions
A = [1, 2, 3]
B = (4, 5, 6)
C = {7, 8, 9}
L = [a for a in A] + [b for b in B] + [c for c in C]
print(L)
# [1, 2, 3, 4, 5, 6, 8, 9, 7]


# Use the asterisk as prefix of iterables to unpack their items
D = {'first': 1, 'second': 2, 'third': 3}

print(*D)
# first second third

# print(**D)
# TypeError: 'first' is an invalid keyword argument for print()

print('{first},{second},{third}'.format(**D))
# 1,2,3


# Extended Iterable Unpacking
L = [1, 2, 3, 4, 5, 6, 7, 8]
a, *b = L
print(a)
# 1
print(b)
# [2, 3, 4, 5, 6, 7, 8]