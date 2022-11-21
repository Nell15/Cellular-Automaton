# Cellular-Automaton

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Presentation

This program allows you to generate an image with any amount of lines from a given line and rule. This process is called a cellular automaton and uses the current state of cells to deduce the following ones.

[Rule 110](https://en.wikipedia.org/wiki/Rule_110) for example is a well known cellular automaton which works using the following principle :
![](https://upload.wikimedia.org/wikipedia/commons/b/b5/One-d-cellular-automaton-rule-110.gif)


## Examples
### Rule 110
Here is an example of the kind of results you can expect using Rule 110.
### Rule 57
Here's a pyramid created using a starting line containing a single black pixel and Rule 57.
![image info](https://cdn.discordapp.com/attachments/719555155632324690/1044032073675063296/image.png)

### Rule 90
Using a starting line containing a single black pixel and Rule 90 creates a figure that looks like a Sierpiński triangle.
![image info](https://cdn.discordapp.com/attachments/719555155632324690/1044022789193093302/image.png)

### More ?
There are many more possible rules (like 30 or 184 which are already in the code but not shown above) and you are more than welcome to use other ones or even create your own.


## Install
All you have to do is download the code and comment or uncomment the needed lines to choose a rule and maybe change the start line.
The code has comments to guide you in modifying those lines

### Dependencies
You need to have mathplotlib installed in order for the code to work.

### Important

My lists have the numbers "reversed" compare to what you may see one Wikipedia. That is because of the way I structured my code at the moment.
That being said, using rule 110 for instance, this is what it would look like :
|    |      111	| 110|	101|	100|	011|	010|	001|	000|
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| Rule |0|	1|	1|	0|	1|	1|	1|	0|
| My code |1|	0|	0|	1|	0|	0|	0|	1|
