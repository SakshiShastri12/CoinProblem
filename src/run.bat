@echo off
echo                     *US COIN SYSTEM*
echo GREEDY APPROACH FOR US COIN SYSTEM
python Greedy.py 11 4 "[1,5,10,25]"
python Greedy.py 23 4 "[1,5,10,25]"
python Greedy.py 31 4 "[1,5,10,25]"
python Greedy.py 51 4 "[1,5,10,25]"
python Greedy.py 73 4 "[1,5,10,25]"
python Greedy.py 83 4 "[1,5,10,25]"
python Greedy.py 91 4 "[1,5,10,25]"
python Greedy.py 99 4 "[1,5,10,25]"

echo RECURSIVE APPROACH FOR US COIN SYSTEM
python Recursive.py 11 4 "[1,5,10,25]"
python Recursive.py 23 4 "[1,5,10,25]"
python Recursive.py 31 4 "[1,5,10,25]"
python Recursive.py 51 4 "[1,5,10,25]"
python Recursive.py 73 4 "[1,5,10,25]"
python Recursive.py 83 4 "[1,5,10,25]"
python Recursive.py 91 4 "[1,5,10,25]"
python Recursive.py 99 4 "[1,5,10,25]"

echo DYNAMIC APPROACH FOR US COIN SYSTEM
python Dynamic.py 11 4 "[1,5,10,25]"
python Dynamic.py 23 4 "[1,5,10,25]"
python Dynamic.py 31 4 "[1,5,10,25]"
python Dynamic.py 51 4 "[1,5,10,25]"
python Dynamic.py 73 4 "[1,5,10,25]"
python Dynamic.py 83 4 "[1,5,10,25]"
python Dynamic.py 91 4 "[1,5,10,25]"
python Dynamic.py 99 4 "[1,5,10,25]"



echo                   *WEIRD COIN SYSTEM*
echo GREEDY APPROACH FOR WEIRD COIN SYSTEM
python Greedy.py 69 5 "[1,5,10,23,25]"
echo RECURSIVE APPROACH FOR WEIRD COIN SYSTEM
python Recursive.py 69 5 "[1,5,10,23,25]"
echo DYNAMIC APPROACH FOR WEIRD COIN SYSTEM
python Dynamic.py 69 5 "[1,5,10,23,25]"

pause 
