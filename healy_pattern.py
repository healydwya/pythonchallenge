import sys
import fileinput 

file_name = sys.stdin
patternArray = []
pathArray = []
pathLooped = False

def readFile(file):
    for line in file:
        try: int(line)
        except ValueError:
            if len(patternArray) < arrayLength:
                patternArray.append(str(line).replace('\n', ''))
            else:
                pathArray.append(str(line).replace('\n', ''))
                
        else: 
            arrayLength = int(line)

    print patternArray
    print pathArray

    write = sys.stdout.write
    write(file.read())

readFile(file_name)