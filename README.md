heapq: A tool to prioritize among to-do's
===============================================================================

heapq is a tool which takes the things you need to do, associated with priority 
levels, and maintains a dynamic to-do list.  We provide three commands: pushq, 
popq and peekq.  pushq lets you add things to the to-do list. It takes a note 
and an associated priority value.

peekq lets you see the to-do list. By default it shows the highest priority 
item in the to-do list, but it can also show the entire list ordered by 
priority.  popq shows the highest priority item and removes it from the to-do 
list.


Building and installing
===============================================================================

heapq is a Python 3 script written using NOWEB literate programming. To compile 
it there is an accompanying Makefile, so compilation is as easy as running 
`make`. This will give you the following files:

 - `heapq` which is the main file.
 - `pushq`, `popq`, `peekq`; which are symbolic links to `heapq`.
 - `heapq.pdf` which is the documented source code.
