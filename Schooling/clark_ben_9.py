# Ben Clark
# CSCI II 161 L03
# Assignment 9


import csv


print()
print('                --- Hello! ---')
userFile = input('Please enter the name of the .tsv file: ')
userFile = userFile.lower()


### begin tsv to txt conversion
tsv_file = open(userFile)
txt_file = open('readme.txt', 'w')
read_tsv = csv.reader(tsv_file, delimiter="\t")


for row in read_tsv:
    joined_string = "\t".join(row)
    txt_file.writelines(joined_string+'\n')
txt_file.close()
tsv_file.close()
### tsv to txt conversion complete


### open created readme.txt and do some formatting
with open(r'readme.txt', 'r+') as file:
    content = file.readlines()
    t = 0
    i = t
    for i in range(len(content)):
        if len(content) > 20:
            print('Only 20 students expected in a class.\n')
            input('Press "Enter" to exit program')
            exit
        elif len(content) < 1:
            print('There are no students in this class.\n')
            input('Press "Enter" to exit program')
            exit
    
        content[t] = content[t].split('\t')
        content[t][4] = content[t][4][:2]

        print('')
        
        midterm1 = int(content[t][2])
        midterm2 = int(content[t][3])
        finalExam = int(content[t][4])
        avgGrade = (midterm1 + midterm2 + finalExam) / 3
        letterGrade = ''

        if avgGrade >= 90:
            letterGrade = 'A'
            content[t].append(letterGrade)
        elif avgGrade < 90 and avgGrade >= 80:
            letterGrade = 'B'
            content[t].append(letterGrade)
        elif avgGrade < 80 and avgGrade >= 70:
            letterGrade = 'C'
            content[t].append(letterGrade)
        elif avgGrade < 70 and avgGrade >= 60:
            letterGrade = 'D'
            content[t].append(letterGrade)
        elif avgGrade < 60:
            letterGrade = 'F'
            content[t].append(letterGrade)
        print(*content[t], sep='    ')           
        t += 1
### finished readme.txt formatting
 
 
### now write the lines to the txt file with formatting           
with open(r'readme.txt', 'w') as f:
    t = 0
    for i in range(len(content)):
        f.write(str(content[t]))
        f.write('\n')
        t += 1
### end of writing to file