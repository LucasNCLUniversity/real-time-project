#imports
import datetime
import re #for splitting the string

#this function splits datetime.now() into seperate values (day, month, year, time)
def dateSplit():
    delimiters = '-', ' ', ':'
    current = str(datetime.datetime.now())
    regexPattern = '|'.join(map(re.escape, delimiters))
    listedTime = re.split(regexPattern, current)
    return listedTime #order of list goes [year, month, day, hour, minute, second]
