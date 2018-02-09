def IncrementalCount(counts, line, charList):

    # Iterating through each element in charList
    for i in charList:
        # If element not in counts then reinitialise counts as zero
        if i not in counts:
            counts[i] = 0
    for i in line:
        # If element in counts then increment counts by 1
        if i in counts: 
            counts[i] += 1
    return counts

def CountDepth(lines):
    # Implement this function for Step 2
    # Initializing counts dictionary, chars string and lineList list
    counts, chars, lineList = {}, "{}", []

    # Iterating over each line in lines variable
    for line in lines:
        # Run IncrementalCount function using variables for each line
        counts = IncrementalCount(counts, line, chars)
        # Checking depth by counting and subtracting count of brackets defined in chars variable
        depth = counts[chars[0]] - counts[chars[1]]
        # Appending depth for each line to lineList
        lineList.append(depth) if depth >= 1 else lineList.append(0)

    return(lineList)

def CreatePythonCode(filename):

    inFileLines, outFileLines = [], []

    # Opening filename and appending each line to inFileLines list
    with open(filename + '.bpy', 'r') as inFile:
        for i in inFile:
            inFileLines.append(i)
    inFile.close()

    listDepth = CountDepth(inFileLines)
    # x variable used as a int operator for checking depth and multiplying indentation depending on depth
    x = 0

    for i in range(0, len(inFileLines)):
        # Striping whitespace from the left
        inFileLines[i] = inFileLines[i].lstrip(" ")
        # List depth begins at 1 for first opening brace found when running CountDepth function
        if listDepth[i] - x == 1:
            # Splitting brace from inFileLines list
            lineSplit = inFileLines[i].split("{")
            # Reassigning new value with indentation and colon at end of line
            inFileLines[i] = x * "   " + lineSplit[0] + ":\n"
        # Checking for closing braces
        elif x - listDepth[i] == 1:
            lineSplit = inFileLines[i].split("}")
            if lineSplit[0] != "":
                inFileLines[i] = x * "   " + lineSplit[0] + "\n"
            else:
                inFileLines[i] = lineSplit[0]
        # If no change in depth append line with same leading amount of indentation
        elif listDepth[i] == x:
            inFileLines[i] = x * "   " + inFileLines[i]
        # Reassigning depth value to x
        x = listDepth[i]
        # Appnending new inFileLines line to outFileLines list
        outFileLines.append("%s" % inFileLines[i])

    # Writing outFileLines to same filename function read in
    with open(filename + '.py', 'w') as outFile:
        for i in outFileLines:
            outFile.write(i)
    outFile.close()
    return()

def IgnoreCommentsAndStrings(s):
    lineList, chars  = [], ["\"", "#"]
    string1, string2, string3, splitString = str(), str(), str(), str()
    flag, flag1 = 0, 0

    # For loop to complete string3
    for i in range(len(s)):
        # Checking each individual char in string s against chars list
        if s[i] == chars[0]:
            # Flagging each time value in s matches chars[0] - backslash
            flag += 1
        # Checking s value if it matches chars[1] - # and checking if flag value is even
        if s[i] == chars[1] and flag % 2 == 0:
            # Assign 1 to flag1 so string is ot split here
            flag1 = 1
        # assign values to splitString if flag1 is zero
        if flag1 == 0:
            splitString += s[i]
        else:
            string3 += s[i]
    # Reinitializing flag variable to zero
    flag = 0

    # Iterating over splitString variable to divide into either string1 or string2
    for i in splitString:
        if i != chars[0]:
            if flag % 2 == 0:
                string1 += i
            string2 += i
        else:
            flag += 1
            string2 += i

    # Adding string1 to string3 to lineList
    lineList.extend([string1, string2, string3])

    return(lineList)

def CreatePythonCodeAdvanced(filename):
    inFileTwo = open("middlefile.bpy","r")
    lines, linesTwo, lineListOne, lineListTwo, outFileLines, chars = [], [], [], [], [], ["\"", "#", "{", "}"]
    original = 0

    # Appending lines of inFileOne to lines list
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
                if x == chars[0]:
                    flag += 1
                if flag % 2 == 0 and x == chars[2]:
                    x = ":"
                string1 += x
            string1=original * "   " + string1
        elif original - list2[i] == 1:
            for x in linesTwo[i]:
                if x == chars[0]:
                    flag += 1
                if flag % 2 == 0 and x == chars[3]:
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
