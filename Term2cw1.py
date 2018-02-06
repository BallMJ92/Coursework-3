def IncrementalCount(counts, line, charList):
    for i in charList:
        if i not in counts: 
            counts[i] = 0
    for i in line:
        if i in counts: 
            counts[i] += 1
    return(counts)

def CountDepth(lines):
    # Implement this function for Step 2
    counts, chars, lineList = {}, "{}", []

    for line in lines:
        counts = IncrementalCount(counts, line, chars)
        depth = counts[chars[0]] - counts[chars[1]]
        lineList.append(depth) if depth >= 1 else lineList.append(0)

    return(lineList)

def CreatePythonCode(filename):
    inFileLines, outFileLines = [], []

    with open(filename + '.bpy', 'r') as inFile:
        for i in inFile:
            inFileLines.append(i)
    inFile.close()

    listDepth = CountDepth(inFileLines)
    x = 0

    for i in range(0, len(inFileLines)):
        inFileLines[i] = inFileLines[i].lstrip(" ")
        if listDepth[i] - x == 1:
            lineSplit = inFileLines[i].split("{")
            inFileLines[i] = x * "   " + lineSplit[0] + ":\n"
        elif x - listDepth[i] == 1:
            lineSplit = inFileLines[i].split("}")
            if lineSplit[0] != "":
                inFileLines[i] = x * "   " + lineSplit[0] + "\n"
            else:
                inFileLines[i] = lineSplit[0]
        elif listDepth[i] == x:
            inFileLines[i] = x * "   " + inFileLines[i]
        x = listDepth[i]
        outFileLines.append("%s" % inFileLines[i])

    with open(filename + '.py', 'w') as outFile:
        for i in outFileLines:
            outFile.write(i)
    outFile.close()
    return()

def IgnoreCommentsAndStrings(s):
    lineList = []
    string1, string2, string3, splitString = str(), str(), str(), str()
    flag, flag1 = 0, 0

    for i in range(len(s)):
        if s[i] == "\"":
            flag += 1
        if s[i] == "#" and flag % 2 == 0:
            flag1 = 1
        if flag1 == 0:
            splitString +=s[i]
        else:
            string3 += s[i]
    flag = 0
    for i in splitString:
        if i != "\"":
            if flag % 2 == 0:
                string1 += i
            string2 += i
        else:
            flag += 1
            string2 += i

    lineList.append(string1)
    lineList.append(string2)
    lineList.append(string3)

    return(lineList)

def CreatePythonCodeAdvanced(filename):
    inFileTwo = open("middlefile.bpy","r")
    lines, linesTwo, lineListOne, lineListTwo, outFileLines = [], [], [], [], []
    original = 0

    with open(filename + ".bpy", "r") as inFileOne:
        for i in inFileOne:
            lines.append(i)
    inFileOne.close()

    with open("middlefile.bpy","w") as outFileOne:
        for line in lines:
            lineListOne = IgnoreCommentsAndStrings(line)
            lineListTwo.append(lineListOne[0])
            outFileOne.write("%s" % (lineListOne[1]+lineListOne[2]))
    outFileOne.close()

    list2 = CountDepth(lineListTwo)

    with open(filename + ".bpy", "r") as inFileTwo:
        for i in inFileTwo:
            linesTwo.append(i)
    inFileTwo.close()

    for i in range(len(linesTwo)):
        string1 = str()
        flag = 0
        linesTwo[i] = linesTwo[i].strip(" ")
        if list2[i] - original == 1:
            for x in linesTwo[i]:
                if x == "\"":
                    flag += 1
                if flag % 2 == 0 and x == "{":
                    x = ":"
                string1 += x
            string1=original * "   " + string1
        elif original - list2[i] == 1:
            for x in linesTwo[i]:
                if x == "\"":
                    flag += 1
                if flag % 2 == 0 and x == "}":
                    x = ""
                if x == " ":
                    x = ""
                string1 += x
            string1 = original * "   " + string1
            if string1 == original * "   " + "\n":
                string1 = ""
        elif list2[i] == original:
            string1 = original * "   " + linesTwo[i]
        original = list2[i]
        outFileLines.append("%s" % string1)

    with open(filename+".py","w")as outFileTwo:
        for i in outFileLines:
            outFileTwo.write(i)
    outFileTwo.close()

    return()
