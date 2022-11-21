"""
cellularAutomaton.py
@author: TRUONG - Nell
"""

###----- Imports -----

import matplotlib.image as pimg
import matplotlib.pyplot as plt
import random

###----- Important -----
# Please read README.md for more details.

###----- CELLULAR AUTOMATON -----

def rules(rule:list, cell1:int, cell2:int, cell3:int)->int:
    """Determines the state of the child cell (0 : black or 1 : black), 
    depending on parent cells and the rule that is used"""
    if cell1 == 0 and cell2 == 0 and cell3 == 0:
        return rule[0]
    if cell1 == 0 and cell2 == 0 and cell3 == 1:
        return rule[1]
    if cell1 == 0 and cell2 == 1 and cell3 == 0:
        return rule[2]
    if cell1 == 0 and cell2 == 1 and cell3 == 1:
        return rule[3]
    if cell1 == 1 and cell2 == 0 and cell3 == 0:
        return rule[4]
    if cell1 == 1 and cell2 == 0 and cell3 == 1:
        return rule[5]
    if cell1 == 1 and cell2 == 1 and cell3 == 0:
        return rule[6]
    if cell1 == 1 and cell2 == 1 and cell3 == 1:
        return rule[7]

def nextGen(rule:list, line:list)->list:
    """Determines the next line depending on a given line and 
    the rule that is used"""
    nextLine = [1] * len(line)
    for column in range(0, len(line)):
        # Selection for the first cell
        if column == 0:
            c1 = line[-1]
            c2, c3 = line[column : column + 2]
        # Selection for the last cell
        elif column == len(line) - 1:
            c1, c2 = line[column - 1 : column + 1]
            c3 = line[0]
        # Selection for middle cells
        else:
            c1, c2, c3 = line[column - 1 : column + 2]
        
        # Updating cells
        nextLine[column] = rules(rule, c1, c2, c3)
    return nextLine

def cellularAutomaton(rule:list, line:list, n:int)->list:
    """Generates a picture with n lines from a given line and ruleset"""
    image = [line]
    nextLine = line
    for i in range(n):
        nextLine = nextGen(rule, nextLine)
        image.append(nextLine)
    return image

###----- Rulesets -----

# Important :Rulesets must be lists containing 8 integers which can either be 1 or 0.
rule30 = [1, 1, 1, 0, 0, 0, 0, 1]
rule90 = [1, 0, 1, 0, 0, 1, 0, 1]
rule57 = [1, 1, 0, 0, 0, 1, 1, 0]
rule110 = [1, 0, 0, 1, 0, 0, 0, 1]
rule184 = [0, 1, 0, 0, 0, 1, 1, 1]

###----- Tests -----

# This will be our start line, you may modify it for different results.
# Here I'll be using the example shown the Rule 110 Wikipedia page
l = [0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0]

# Here's an example that is more relevant for rules 30, 57 and 90
# l = [1] * 50 + [0] + [1] * 50

# This will be number of lines in the final picture, you may modify it for different results.
n = 100

# You may comment or uncomment the next lines to select the rule you want. You can also add your own.
# image = cellularAutomaton(rule30, l, n)
# image = cellularAutomaton(rule57, l, n)
image = cellularAutomaton(rule90, l, n)
# image = cellularAutomaton(rule110, l, n)
# image = cellularAutomaton(rule184, l, n)

###----- Result display -----

plt.imshow(image, cmap = 'gray', clim = (0, 1))
plt.show()