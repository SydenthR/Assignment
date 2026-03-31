# Name: Alex Russell
# File Name: student_gpa_checker.py
# Description: This program accepts student names and GPAs, then determines if the student qualifies for the Dean's List or Honor Roll.

while True:
    # Ask for last name
    last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
    
    # Check if user wants to quit
    if last_name == 'ZZZ':
        print("Exiting program...")
        break

    # Ask for first name
    first_name = input("Enter student's first name: ")

    # Ask for GPA
    gpa = float(input("Enter student's GPA: "))

    # Check for Dean's List
    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List.")
    
    # Check for Honor Roll
    elif gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll.")
    
    else:
        print(first_name, last_name, "did not qualify for honors.")