# Cellular Automaton

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Presentation

This program allows you to generate an image with any amount of lines from a given line and rule. This process is called a cellular automaton and uses the current state of cells to deduce the following ones.

[Rule 110](https://en.wikipedia.org/wiki/Rule_110) for example is a well known cellular automaton which works using the following principle :
|![](https://upload.wikimedia.org/wikipedia/commons/b/b5/One-d-cellular-automaton-rule-110.gif)|
|:--:|
|An animation of the way the rules of a 1D cellular automaton determine the next generation, using Rule 110.
Credits : Cormullion (Wikipedia)|

## Static images examples
### Rule 110
Here is an example of the kind of results you can expect using Rule 110.
<p align="center">
  <img src="https://media.discordapp.net/attachments/719555155632324690/1042890938592284683/image.png"/>
</p>

### Rule 57
Here's a pyramid created using a starting line containing a single black pixel and Rule 57.
<p align="center">
  <img src="https://cdn.discordapp.com/attachments/719555155632324690/1044032073675063296/image.png"/>
</p>

### Rule 90
Using a starting line containing a single black pixel and Rule 90 creates a figure that looks like a Sierpiński triangle.
<p align="center">
  <img src="https://cdn.discordapp.com/attachments/719555155632324690/1044022789193093302/image.png"/>
</p>

### More ?
There are many more possible rules (like 30 or 184 which are already in the code but not shown above) and you are more than welcome to use other ones or even create your own.

## Animated generation
Here's a visualization of the previous example (see rule 90) being built, layer by layer.
<p align="center">
  <img src="https://cdn.discordapp.com/attachments/719555155632324690/1047252310394413226/animation.gif"/>
</p>

## Install
All you have to do is download the code and comment or uncomment the needed lines to choose a rule and maybe change the start line.
The code has comments to guide you in modifying those lines.

### Dependencies
You need to have matplotlib installed in order for the code to work.
#### Animation
In order for the animation script to work, make sure that both scripts are located in the same folder.

### Important

My lists have the numbers "reversed" compare to what you may see one Wikipedia. That is because of the way I structured my code at the moment.
That being said, using rule 110 for instance, this is what it would look like :
|    |      111	| 110|	101|	100|	011|	010|	001|	000|
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| Rule |0|	1|	1|	0|	1|	1|	1|	0|
| My code |1|	0|	0|	1|	0|	0|	0|	1|
