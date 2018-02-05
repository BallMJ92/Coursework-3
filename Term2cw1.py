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
    counts, chars, lineList = {}, "{}", []

    for line in lines:
        counts = IncrementalCount(counts, line, chars)
        depth = counts[chars[0]] - counts[chars[1]]
        lineList.append(depth) if depth>=1 else lineList.append(0)

    return(lineList)


def CreatePythonCode(filename):
    # Implement this function for Step 3
    inFileLines = []
    outFileLines = []
    cDepth = []
    indentation = []
    file = ""
    characters = ("{", "}")
    replacements = (":", "")

    with open(filename+'.bpy', 'r') as inFile:
        for i in inFile:
            inFileLines.append(i)

    inFile.close()
    for i in inFileLines:
        cDepth = CountDepth(inFileLines)

    print(cDepth)

    for i in inFileLines:
        x = len(i) - len(i.lstrip(" "))
        indentation.append(x)




    inFileLines = [i.lstrip(" ") for i in inFileLines]

    for i in inFileLines:
        if i[len(i) - 3:len(i)] == "{}\n":
            outFileLines.append(i)
        else:
            n = i.replace("{", ":").replace("}", "")
            outFileLines.append(n)


    for i in range(len(cDepth)):
        for x in outFileLines:
            if cDepth[i] > 1 and cDepth[i-1] == 1:
                print("yes")
                #x.insert(0, "   "*cDepth[i])




    with open("testing3"+'.py', 'w') as outFile:
        for i in outFileLines:
            outFile.write(i)

    outFile.close()

    return ()


def IgnoreCommentsAndStrings(s):
    # Implement this function for Step 4
    return ()


def CreatePythonCodeAdvanced(filename):
    # Implement this function for Step 5
    return ()
