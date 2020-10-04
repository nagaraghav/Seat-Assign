import csv
import sys 
import re


"""[summary]

"""
def readRosterWithCondition(myf, filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for i, row in enumerate(csv_reader):
            print(i)
            if line_count == 0:
                line_count += 1
            else:
                if(len(row) != 4):
                    print("Missing information in roster on row: ", i)

                if(myf(row)):
                    print(row)
                
                line_count += 1


"""[summary]
Creates and returns a function to check if student's GPA is within desired range



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
"""
def createEmailCondition(pat):
    print(pat)
    def gpaf(row): 
        matchObj = re.search(pat, row[2].lower())
        if matchObj:
            return True
        else:
            return False
    return gpaf


"""[summary]
Creates and returns a function to check if student's name matches pattern
"""
def createNameCondition(pat):
    
    def gpaf(row): 
        
        matchObj_first = re.search(pat, row[0].lower())
        matchObj_last = re.search(pat, row[1].lower())
        if matchObj_first or matchObj_last:
            return True
        else:
            return False
    return gpaf




def main():
    if len(sys.argv) < 3:
        print("Too few arguments. Please pass in command and file.")

    command = sys.argv[1]
    filename = sys.argv[2]

    com, pattern = command.split(" ", 1)
    
    
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