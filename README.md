# PasswordHunting
Find passwords for your shared network folders.

First you have to find shared folders on your network. (\\192.168.2.3\folder, etc.) Then make these \\IP\Folder file with newline separated. Your second file has to have keywords that you want to search. (password, pwd, passwd, etc.) 

This program goes recursively folders and when it hits a file opens it then search for your keywords. If keyword is found on the file, it prints the output a txt file like <b> found "Keyword" in \\\\{ip}\folder1\folder2\folder3\file.something </b>

FoundWithoutLine.py file runs quick because it doesn't read line by line. This will cause the results will be just ip, folder and file names with founded keyword information. 

If you want to see which line contains the matching keyword, then run the FoundWithLine.py file. You can use them together like, first run FoundWithoutLine.py then take the results and make those results FoundWithLine.py's input. So you will just scanning the keywords matching files with FoundWithLine.py .

<h4>Usage</h4>

> <b><i>FoundWithoutLine.py   ip_folders_file.txt   keywords.txt</b></i>

Output will be txt format. Second python file will output the matching line. It's usage is similar to the first one. Output of the first FoundWithoutLine.py programs output will be the input of the second FoundWithLine.py program. (Note: Make sure that you delete <b>found *Keyword* in file</b> in the output txt file. Second pyhton program just needs \\\\ip\folder1\folder2\file.something endpoint.)

> <b><i>FoundWithLine.py   ip_folders_files.txt   keywords.txt</b></i>
