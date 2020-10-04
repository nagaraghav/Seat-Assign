import csv
import sys
import re


"""[summary]
Reads the CSV file row by row, and checks if eah student meets the passed in condition or not. If it matches, prints student details to terminal.

myf - condition function 
filename - Name of CSV file of Roster
"""


def readRosterWithCondition(myf, filename):

    try:
        myfile = open(filename) 
    except IOError:
        print("Could not open file. Plese check file name.")
        return

    with myfile as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for i, row in enumerate(csv_reader):

            if i > 0:
                # Makes sures each row has 4 columns for student details (firstname, lastname, email, gpa)
                if(len(row) != 4):
                    print("Missing information in roster on row: ", i)

                # If meets condition, print student details to terminal
                if(myf(row)):
                    print(row)

                


"""[summary]
Creates and returns a function to check if student's GPA is within desired range

pat - pattern entered by user (gpa including + or -)
"""


def createGpaCondition(pat):

    gpa = pat[:-1]
    sign = pat[-1]

    gpa = float(gpa)

    if sign == "+":
        def gpaf(row):
            return float(row[-1]) > gpa
        return gpaf
    else:
        def gpaf(row):
            return float(row[-1]) < gpa
        return gpaf


"""[summary]
Creates and returns a function to check if student's email matches pattern

pat - regualar expression pattern entered by user 
"""


def createEmailCondition(pat):
    pat = pat.lower()
    def gpaf(row):
        matchObj = re.search(pat, row[2].lower())
        if matchObj:
            return True
        else:
            return False
    return gpaf


"""[summary]
Creates and returns a function to check if student's name matches pattern

pat - regualar expression pattern entered by user 

"""


def createNameCondition(pat):
    #Lowercase pattern, because we want case insensitive search
    pat = pat.lower()
    def gpaf(row):

        matchObj_first = re.search(pat, row[0].lower())
        matchObj_last = re.search(pat, row[1].lower())
        if matchObj_first or matchObj_last:
            return True
        else:
            return False
    return gpaf


"""[summary]
Reads the entered arguments, creates a myCondition function and passes it on to readRosterWithCondition

python3 seats.py [command] [roster csv filename]

"""


def main():
    if len(sys.argv) < 3:
        print("Too few arguments. Please pass in command and file.")

    #get the 2 arguments 
    command = sys.argv[1]
    filename = sys.argv[2]

    #breaks down command into command and pattern
    com, pattern = command.split(" ", 1)



    #make myCondition according to command
    myCondition = None
    if(com == "-gpa"):
        myCondition = createGpaCondition(pattern)
    elif(com == "-email"):
        myCondition = createEmailCondition(pattern)
    elif(com == "-name"):
        myCondition = createNameCondition(pattern)
    else:
        print("No matching command.")
        return

    readRosterWithCondition(myCondition, filename)


if __name__ == "__main__":
    main()
