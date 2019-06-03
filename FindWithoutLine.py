import os
import sys
import re

def walk_error_handler(exception_instance):
    print("File can't be accessed")

output = open('utf8-10.txt', 'a')
output.write('\n')
fileList = []
shareList = open(sys.argv[1])
eachShare = shareList.readlines();
for shares in eachShare:
    path = shares.rstrip('\r\n')
    print '\nWalking directory ' + path + '\n'
    for root, subFolders, files in os.walk(path, onerror=walk_error_handler):
        for file in files:   
            fileList.append(os.path.join(root,file))
            print 'Found ' + root + file
keywords = open(sys.argv[2])
searchTerm = keywords.readlines();
output.write('\n\n=== Files matching search criteria ===\n\n')
for item in fileList:
    item = item.strip('\r\n')
    check = os.path.isfile(item)
    if check:
        if os.stat(item).st_size > 70000000:
            continue
        try:
            try:
                searchFile = open(item, 'rb')
            except (OSError, IOError) as e:
                continue
            sf = searchFile.readlines()
            if re.search(r'\\x00',str(sf).decode('UTF-8'), re.IGNORECASE):
                continue
            for term in searchTerm:
                strip = term.strip('\r\n') 
                print 'Searching file ' + item + ' for term ' + term
                if re.search(strip, str(sf).decode('UTF-8'), re.IGNORECASE):
                    output.write('found ' + strip + ' in file ' + item + '\n')
            try:
                searchFile.close()
            except:
                continue
        except (IOError) as e:
            continue
    else:
        continue
output.close()