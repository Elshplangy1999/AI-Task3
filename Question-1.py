# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 22:31:48 2021

@author: Emad Elshplangy
"""

import prolog1 as prolog


#Assignment : Question1 

# (1)
a = prolog.Term("color(carrots,orange)")
print(a, '\n')
print(a.pred, '\n')
print(a.args, '\n')
# (2)
b = prolog.Rule("likes(Person, carrots):-vegetarian(Person)")
print(b, '\n')
print(b.head, '\n')
print(b.goals, '\n')
# (3)
c = prolog.Rule("pass(Student) :- study_hard(Student)")
print(c, '\n')
print(c.head, '\n')
print(c.goals, '\n')
# (4)
# (5)
# (6)
d = prolog.Rule("enemies(X, Y) :- hates(X, Y), fights(X, Y)")
print(d, '\n')
print(d.head, '\n')
print(d.goals, '\n')