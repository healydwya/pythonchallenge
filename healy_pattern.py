import sys
import fileinput 
import re

file_name = sys.stdin

def readFile(file):
    patternArray = []
    pathArray = []
    count = 0
    arraylength = 0
    for line in file:
        if count < 1:
            arraylength = line
            count = count + 1
        else:
            if len(patternArray) < int(arraylength):
                patternArray.append(list(filter(None, line.replace('\n', '').split(','))))
            else:
                pathArray.append(list(filter(None, line.replace('\n', '').split('/'))))

    pathArray = pathArray[1:]

    getMatchingPatterns(patternArray, pathArray)

def getMatchingPatterns(patternArray, pathArray):
    delimeter = ","
    matches = []
    for paths in pathArray:
        matches = []
        for pattern in patternArray:
            if (len(paths) == len(pattern)):
                charMatches = 0
                for index,char in enumerate(paths):
                    if pattern[index] == char or pattern[index] == '*':
                        charMatches = charMatches + 1
                        if len(paths) == charMatches:
                            matches.append(delimeter.join(pattern))
        if len(matches) == 0:
            print "NO MATCH"
        else:
            if len(matches) > 1:
                groupMatches(matches)
            else:
                print matches[0]

def groupMatches(matches):
    lowestCount = None
    currentCount = None
    patternArray = []
    for match in matches:
        currentCount = match.count("*")
        if lowestCount > currentCount or lowestCount == None:
            patternArray = []
            lowestCount = currentCount
            patternArray.append(match)
        elif lowestCount == currentCount:
            patternArray.append(match)
    if len(patternArray) > 1:
        wildcardMatch(patternArray)
    else:
        print patternArray[0]

def wildcardMatch(patternArray):
    lowestIndex = None
    currentIndex = None
    for pattern in patternArray:
        try:
            currentIndex = re.search(r'[^\*]', pattern).start()
            if lowestIndex < currentIndex or lowestIndex == None:
                lowestIndex = currentIndex
        except:
            lowestIndex = 0
    print patternArray[lowestIndex]
            
readFile(file_name)