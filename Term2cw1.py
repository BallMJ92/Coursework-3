# Be sure to read the coursework submission section in the coursework document

"""Saving values from IncrementalCount function outside of function so list does not get cleared
each time function is ran"""
characters = []


def IncrementalCount(counts, line, charList):
    # Implement this function for Step 1

    # Creating list to hold individual characters of line and charList
    lineList = [l for l in line]
    chars = [c for c in charList]

    # Checking if chars in lineList appear in chars list and adding them to global list characters
    for i in range(0, len(lineList)):
        if lineList[i] in chars:
            characters.append(lineList[i])

    # Creating a dictionary from charList with key as chars in charList and value as number of appearances of chars
    counts = dict.fromkeys(charList, 0)
    for i in range(0, len(characters)):
        if characters[i] in counts:
            # Incrementing key value if char appears
            counts[characters[i]] = counts.get(characters[i], 0) + 1

    return counts


def CountDepth(lines):
    # Implement this function for Step 2
    characters.clear()
    counts = {}
    charList = "{}"
    depth = 0
    depths = []
    bracketList = []
    counts = IncrementalCount(counts, str(lines), charList)
    isEven = 0

    for key, value in counts.items():
        bracketList.append(key)
        # Assigning the values of both left and right brackets to isEven variable
        isEven += value

    # Adding lines to list to iterate over
    lineList = [i for i in lines]

    for i in range(0, len(lineList)):
        # Checking if there is an even amount of left and right brackets
        if isEven % 2 == 0:
            # Checking if line contains only a right bracket
            if lineList[i].count(bracketList[0]) >= 1 and lineList[i].count(bracketList[1]) == 0:
                depth += 1
                depths.append(depth)
            # Checking if line contains only a left bracket
            elif lineList[i].count(bracketList[1]) >= 1 and lineList[i].count(bracketList[0]) == 0:
                depth -= 1
                depths.append(depth)
            # Checking if line contains 1 or more left and right brackets
            elif lineList[i].count(bracketList[0]) >= 1 and lineList[i].count(bracketList[1]) >= 1:
                depths.append(depth)
            # If line does not contain brackets append last depth value
            else:
                depths.append(depth)
        else:
            print("Error in code formatting")
            break

    return depths

def CreatePythonCode(filename):
    # Implement this function for Step 3

    """with open(filename+'.bpy', 'r') as inFile:

    return ()"""


def IgnoreCommentsAndStrings(s):
    # Implement this function for Step 4
    return ()


def CreatePythonCodeAdvanced(filename):
    # Implement this function for Step 5
    return ()
