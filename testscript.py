from Term2cw1 import *


counts = {}
counts= IncrementalCount(counts,"{hello!{}","}{#")
counts= IncrementalCount(counts,"#Goodbye!}","}{#!@")

if counts == {'}': 2, '{': 2, '#': 1, '!': 1, '@': 0}:
    print("Step 1: Success!")
else:
    print("Step 1: Failed")


inf = open("translateSimpleDelimeters.bpy", "r")
lines = inf.readlines()
inf.close()
if CountDepth(lines) ==[1, 1, 1, 1, 1, 1, 2, 2, 1, 0, 0, 1, 1, 1, 2, 2, 2, 1, 1, 1, 0, 0]:
    print("Step 2: Success!")
else:
    print("Step 2: Failed")

try:
    CreatePythonCode("translateSimpleDelimeters")
    inf = open("translateSimpleDelimeters.py", "r")
    lines = inf.readlines()
    inf.close()
    inf = open("translateSimple.py", "r")
    linesTrue = inf.readlines()
    inf.close()
    success=True
    for i in range(0, len(lines)):
        if not (lines[i].rstrip()==linesTrue[i].rstrip()):
            success=False

    if success:
        print("Step 3: Success!")
    else:
        print("Step 3: Failed")

except:
    print("Step 3: Failed")



s='outf.write("/#{" + str(num) + "#/ " + line) #lots of hashes(#)  and braces ({{)'
sOut = ['outf.write( + str(num) +  + line) ', 'outf.write("/#{" + str(num) + "#/ " + line) ', '#lots of hashes(#)  and braces ({{)']
if IgnoreCommentsAndStrings(s) == sOut:
   print("Step 4: Success!")
else:
    print("Step 4: Failed")




