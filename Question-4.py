# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 22:36:07 2021

@author: Emad Elshplangy
"""

import aima.utils
import aima.logic

ex = aima.utils.expr
fc = aima.logic.fol_fc_ask


def main():
    clauses = [ex("Man(John)"), ex("Woman(Jia)"), ex("Healthy(John)"), ex("Wealthy(John)"), ex("Wealthy(Jia)"),
               ex("(Wealthy(x) & Healthy(x)) ==> Traveler(x)")]
    KB = aima.logic.FolKB(clauses)
    wealthy = fc(KB, ex('Wealthy(x)'))
    healthy = fc(KB, ex('Healthy(x)'))

    traveler = fc(KB, ex('Traveler(x)'))
    print('Who are healthy ?')
    print(list(healthy), '\n')
    print('Who are wealthy ?')
    print(list(wealthy), '\n')
    print('Who can travel ?')
    print(list(traveler))
    print()


if __name__ == "__main__": main()