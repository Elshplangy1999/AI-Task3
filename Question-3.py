# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 22:34:18 2021

@author: Emad Elshplangy
"""

import prolog1 as prolog

#Assignment : Question3


# 1
# Correct prolog ==> enemies(X,Y):-hates(X,Y),hates(Y,X)
# Python code
a = prolog.Rule("enemies(X,Y):-hates(X,Y),hates(Y,X)")
print(a, '\n')
print(a.head, '\n')
print(a.goals, '\n')
# 2
# Correct prolog ==> p(X):-q(X),r(X)
# Python Code
b = prolog.Rule("p(X):-q(X),r(X)")
print(b, '\n')
print(b.head, '\n')
print(b.goals, '\n')