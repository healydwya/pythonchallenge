import sys
import fileinput 
import re

file_name = sys.stdin

def readFile(file):
    patternArray = []
    pathArray = []
    count = 0
    arraylength = 0
    # sets first list length equal to first integer
    for line in file:
        if count < 1:
            arraylength = line
            count = count + 1
        # filters lists into two separate arrays to compare against each other
        else:
            if len(patternArray) < int(arraylength):
                patternArray.append(list(filter(None, line.replace('\n', '').split(','))))
            else:
                pathArray.append(list(filter(None, line.replace('\n', '').split('/'))))
    
    # removes first integer from second list since it just signifies number of patterns
    pathArray = pathArray[1:]

    getMatchingPatterns(patternArray, pathArray)

def getMatchingPatterns(patternArray, pathArray):
    delimeter = ","
    matches = []
    #compares each pattern to each path
    for paths in pathArray:
        matches = []
        for pattern in patternArray:
            # first check if lengths match
            if (len(paths) == len(pattern)):
                charMatches = 0
                # if lengths match check each character individually, add 1 each time a character matches
                for index,char in enumerate(paths):
                    if pattern[index] == char or pattern[index] == '*':
                        charMatches = charMatches + 1
                        # if the length of the path matches the number of characters that matched, mark as a match
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
    # in new array of potential matches to the path, compare number of wildcards in each match
    for match in matches:
        currentCount = match.count("*")
        # initialize empty pattern array, add pattern(s) with lowest amount of wildcards to it 
        if lowestCount > currentCount or lowestCount == None:
            patternArray = []
            lowestCount = currentCount
            patternArray.append(match)
        elif lowestCount == currentCount:
            patternArray.append(match)
    # if there are multiple matches with equal numbers of wildcards, go on to check positioning of them
    if len(patternArray) > 1 and lowestCount != 0:
        wildcardMatch(patternArray)
    else:
        print patternArray[0]

def wildcardMatch(patternArray):
    highestindex = None
    currentindex = None
    bestpattern = []
    for index, pattern in enumerate(patternArray):
        firstwildcard = pattern.index('*')
        if highestindex == None or highestindex < firstwildcard:
            highestindex = firstwildcard
            bestpattern = index
 
    print patternArray[bestpattern]
            
readFile(file_name)