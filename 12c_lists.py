#from 12class.py:

import re
names=["ria sharma","sachin tendulkar","aaa ddd","a d","123alia","rahul dravid","$#123"]
pattern=r'[a-zA-Z][a-zA-Z" "]+'
print("Valid names are:")

#done by me:
for name in names:
    if re.fullmatch(pattern,name):
        print(name)
    else:
        print(f"{name} is not a valid name")
#fullmatch: It checks if the entire string matches the specified pattern.

#what sir told:
for name in names:
    print(name,bool(re.match(pattern,name)))

"""Write a pattern to find valid variable names in Python."""

variables=["var1","1var","_var","var_2","var-3","var$4","var 5","varName","VarName","varName123"]
pattern=r'[_a-zA-Z][a-zA-Z0-9_]*'
print("\nValid variable names are:")
for var in variables:
    if re.fullmatch(pattern,var):
        print(var,"is valid")
    else:
        print(var,"is invalid")
