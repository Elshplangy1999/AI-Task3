# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 22:31:48 2021

@author: Emad Elshplangy
"""

import prolog1 as prolog

#Assignment : Question2


# 1
# prolog syntax ==> read(Maria,logic_programming,Peter_Lucas)
# Python Code
a = prolog.Term("read(Maria,logic_programming,Peter_Lucas)")
print(a, '\n')
print(a.pred, '\n')
print(a.args, '\n')
# 2
# prolog syntax ==> like(x,shopping):- girl(x)
# Python Code
b = prolog.Rule("like(x,shopping):- girl(x)")
print(b, '\n')
print(b.head, '\n')
print(b.goals, '\n')
# 3
# prolog syntax ==> ?-like_shopping(Who)
# Python Code

# 4
# prolog syntax ==> hates(kirke,x):- is_city(x), is_big(x), is_crowdy(x)
# Python Code
c = prolog.Rule("hates(kirke,x):- is_city(x), is_big(x), is_crowdy(x)")
print(c, '\n')
print(c.head, '\n')
print(c.goals, '\n')