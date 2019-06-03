import os
import sys
import re

def walk_error_handler(exception_instance):
    print("File can't be accessed")

output = open('utf8-10-last1.txt', 'a')
output.write('\n')
fileList = []
f = open(sys.argv[1])
for lines in f.readlines():
    fileList.append(lines)
keywords = open(sys.argv[2])
searchTerm = keywords.readlines()

output.write('\n\n=== Files matching search criteria ===\n\n')
for item in fileList:
    item = item.strip('\r\n')
    check = os.path.isfile(item)
    if check:
        try:
            searchFile = open(item, 'rb')
        except (OSError, IOError) as e:
            continue
        for line in searchFile:
            for term in searchTerm:
                strip = term.strip('\r\n')
                print 'Searching file ' + item + ' for term ' + term
                if re.search(strip, line, re.IGNORECASE):
                    output.write('found ' + strip + ' in file ' + item + ' -> '+ line + '\n')
        try:
            searchFile.close()
        except:
            continue
    else:
        continue
output.close()