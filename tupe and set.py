# Python 3.13.11 (tags/v3.13.11:6278944, Dec  5 2025, 16:26:58) [MSC v.1944 64 bit (AMD64)] on win32
# Enter "help" below or click "Help" above for more information.
# student = ('ali',12,'fasalka 7aad')
# student
# ('ali', 12, 'fasalka 7aad')
# >>> student.append('abdi')
# Traceback (most recent call last):
#   File "<pyshell#2>", line 1, in <module>
#     student.append('abdi')
# AttributeError: 'tuple' object has no attribute 'append'
# >>> dob= (12,'janaayo',2010)
# >>> print(dob)
# (12, 'janaayo', 2010)
# >>> dob
# (12, 'janaayo', 2010)
# >>> print(student[0])
# ali
# >>> print(student[7])
# Traceback (most recent call last):
#   File "<pyshell#7>", line 1, in <module>
#     print(student[7])
# IndexError: tuple index out of range
# >>> print(student[-2])
# 12
# >>> xog = {'xisaab','english','xisaab'}
# >>> xog
# {'xisaab', 'english'}
# >>> xog.add('arabic')
# >>> xog
# {'xisaab', 'arabic', 'english'}
# >>> xog.remove('arabic')
# >>> xog
# {'xisaab', 'english'}
# >>> xog.add('arabic','tarbiyo','soomalia')
# Traceback (most recent call last):
#   File "<pyshell#15>", line 1, in <module>
#     xog.add('arabic','tarbiyo','soomalia')
# TypeError: set.add() takes exactly one argument (3 given)
# >>> xog.add('tarbiyo','soomalia')
# Traceback (most recent call last):
#   File "<pyshell#16>", line 1, in <module>
#     xog.add('tarbiyo','soomalia')
# TypeError: set.add() takes exactly one argument (2 given)
# >>> xog.add('tarbiyo' 'soomalia')
# >>> xog
# {'xisaab', 'english', 'tarbiyosoomalia'}
# >>> xog.add('juqraafi' '' 'islamic')
# # >>> xog
# {'xisaab', 'english', 'juqraafiislamic', 'tarbiyosoomalia'}
# >>> xog.add('juqraafi' " " 'islamic' " "  'java')
# # >>> xog
# {'xisaab', 'english', 'juqraafiislamic', 'juqraafi islamic java', 'tarbiyosoomalia'}