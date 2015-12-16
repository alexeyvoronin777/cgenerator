
.. other page


How to use
==========
::

	cgenerator <type name> <output folder> <is custom> <containers>
	cgenerator uint ../src/ False list,vector
	cgenerator 'struct matrix' ./source/ True list
	
**type name** - C type of entity. It's can be standard type or custom(struct, union and etc.).

**output folder** - Output folder for generated files(*.c, *.h).

**is custom** - can be True or False. 

**containers** - types for generation. It's can be list, vector, hashmap, set

