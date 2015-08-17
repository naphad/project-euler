# check

import os

def is_empty(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            if (i > 1):
                return False
        return True

sol_nums = {}
files = os.listdir(os.curdir)
for f in files:
    if (".py" in f and "check" not in f and "~" not in f):
        sol_nums[int(f[:-3])] = is_empty(f)
print "ALL problems between", min(sol_nums), "and", max(sol_nums), "done EXCEPT" 
for i in range(min(sol_nums), max(sol_nums)+1):
    if i not in sol_nums or sol_nums[i]:
        print "\t", i
print "Done"
