# Seat-Assign


Implementation of Professor Porquet's Seat Assign Project.

Python script which allows you to find students whose name or email matches a given pattern, or whose GPA is within given range.

## To Run:
python3 seats.py [command] [roster csv filename]

## Sample Commands
python3 seats.py "-gpa 3.2+" roster.csv  
python3 seats.py "-name cel" roster.csv  
python3 seats.py "-email \\.(com|net)" roster.csv  

## Implementation:
I made the script modular and broke down the commands into 3 functions which return a 'condition' function to check if a student fits the pattern. 

Once the 'condition' function has been created for the specific command, I am passing it into 'readRosterWithConditiom' function which reads the CSV file and checks if each student/row meets the condition. 

I am using Python's csv library and re, regular expressions, to find pattern of email and name.

