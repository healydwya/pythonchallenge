import sys
import fileinput 
import re

file_name = sys.stdin

def read_file(file):
    pattern_array = []
    path_array = []
    count = 0
    array_length = 0
    # sets first list length equal to first integer
    for line in file:
        if count < 1:
            array_length = line
            count = count + 1
        # filters lists into two separate arrays to compare against each other
        else:
            if len(pattern_array) < int(array_length):
                pattern_array.append(list(filter(None, line.replace('\n', '').split(','))))
            else:
                path_array.append(list(filter(None, line.replace('\n', '').split('/'))))
    
    # removes first integer from second list since it just signifies number of patterns
    path_array = path_array[1:]

    get_matching_patterns(pattern_array, path_array)

def get_matching_patterns(pattern_array, path_array):
    delimeter = ","
    matches = []
    #compares each pattern to each path
    for paths in path_array:
        matches = []
        for pattern in pattern_array:
            # first check if lengths match
            if (len(paths) == len(pattern)):
                char_matches = 0
                # if lengths match check each character individually, add 1 each time a character matches
                for index,char in enumerate(paths):
                    if pattern[index] == char or pattern[index] == '*':
                        char_matches = char_matches + 1
                        # if the length of the path matches the number of characters that matched, mark as a match
                        if len(paths) == char_matches:
                            matches.append(delimeter.join(pattern))
        if len(matches) == 0:
            print("NO MATCH")
        else:
            if len(matches) > 1:
                group_matches(matches)
            else:
                print(matches[0])

def group_matches(matches):
    lowest_count = None
    current_count = None
    pattern_array = []
    # in new array of potential matches to the path, compare number of wildcards in each match
    for match in matches:
        current_count = match.count("*")
        # initialize empty pattern array, add pattern(s) with lowest amount of wildcards to it 
        if lowest_count == None or lowest_count > current_count:
            pattern_array = []
            lowest_count = current_count
            pattern_array.append(match)
        elif lowest_count == current_count:
            pattern_array.append(match)
    # if there are multiple matches with equal numbers of wildcards, go on to check positioning of them
    if len(pattern_array) > 1 and lowest_count != 0:
        wildcard_match(pattern_array)
    else:
        print(pattern_array[0])

def wildcard_match(pattern_array):
    highest_index = None
    current_index = None
    best_pattern = []
    for index, pattern in enumerate(pattern_array):
        first_wildcard = pattern.index('*')
        if highest_index == None or highest_index < first_wildcard:
            highest_index = first_wildcard
            best_pattern = index
 
    print(pattern_array[best_pattern])
            
read_file(file_name)