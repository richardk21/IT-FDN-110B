# -------------------------------------------------------- #
# Title: Assignment05
# Desc: This assignment demonstrates data processing using dictionaries and files
# Change Log: (Who, When, What)
# RichardK, 11/13/2023, Created Script
# ----------------------------------------------------------#

import json

# Define the Data Constants
MENU: str =\
    "--Course Registration Program--\n\
Select from the following menu\n\
1. Register a Student for a Course\n\
2. Show current data\n\
3. Save data to a file\n\
4. Exit the program"

FILE_NAME: str = 'Enrollments.json'

# Define the Data Variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
file_obj = None
menu_choice: str = ''
student_data: dict = {}
students: list = []

# When the program starts, read the file data into a list of dictionary rows (table)
try:
    file_obj = open(FILE_NAME, "r")
    student = json.load(file_obj)
    file_obj.close()
except Exception as e:
     print("Please check that the file exist")
     print(e.__doc__)
     print(e.__str__())
finally:
    file_obj.close()

# Present and Process the data
while True:

    # Present the menu of choices
      print(MENU)
      menu_choice = str(input("Enter a menu option (1-4): "))

    # Option 1: Input user data
      if menu_choice == "1":

        try:
            student_first_name = input("What is the student_first_name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("What is the student_last_ name?")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("What is the course name?")
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print("Error Message")
            print(e.__doc__)
            print(e.__str__)
        continue

    # Option 2: Present the current data
      elif menu_choice == "2":
        print ("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
            print("-" * 50)
            continue

      # Save the data to a file
      elif menu_choice == "3":

          try:
               file_obj = open(FILE_NAME, 'w')
               json.dump(student, file_obj)
               file_obj.close()
               print("The following data was saved")
               for student in students:
                    print(f"Student {student_first_name},{student_last_name},is already enrolled in {course_name}")

          except Exception as e:
              print(f"An error occured: {e}")

    # Stop the loop
      elif menu_choice == "4":
          # Exit the loop and end the program
          break

