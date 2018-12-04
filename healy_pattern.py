import sys
import fileinput 
import re

file_name = sys.stdin

def readFile(file):
    patternArray = []
    pathArray = []
    for line in file:
        try: int(line)
        except ValueError:
            if len(patternArray) < arrayLength:
                patternArray.append(list(filter(None, line.replace('\n', '').split(','))))
            else:
                pathArray.append(list(filter(None, line.replace('\n', '').split('/'))))
        else: 
            arrayLength = int(line)

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
        print pattern
        try:
            currentIndex = re.search(r'[^*]', pattern).start()
            if lowestIndex < currentIndex or lowestIndex == None:
                lowestIndex = currentIndex
        except:
            return
    try:
        print patternArray[lowestIndex]
    except:
        return
            
readFile(file_name)