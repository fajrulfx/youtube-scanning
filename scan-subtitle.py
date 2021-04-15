import os
import re

src_dict = ("/path") #Specify base directory
keyword = ['Keyword1','Keyword2','Keyword3','Keyword4']
pattern = re.compile('|'.join(keyword),re.IGNORECASE)

output = open("Result.txt", "a")

for yum_files in os.listdir(src_dict): # obtain list of files in directory
    files = os.path.join(src_dict, yum_files) #join the full path with the names of the files.
    strng = open(files, encoding='windows-1252') #We need to open the files
    for lines in strng.readlines(): #We then need to read the files
        if re.search(pattern, lines): #If we find the pattern we are looking for
            print(yum_files)
            output.write(yum_files)
            output.write("\n")
            break
