# Name: Maria Traskowsky
# Section: (C) TU 11:00am - 12:15pm
# Project: Student Grading
# Description: This program uses dictionaries and lists to store student info such as
# name, ID, number of assignments, and each score for the assignments. The program
# also displays the average score of each student.

from collections import defaultdict
x = True
student_num = 1
student_list = {}
avg_score = 0
assignment_total = 0
#scores = []
while x:
    # value
    print()
    student_name = input("Enter student name for Student " + str(student_num) + ": ")

    # key
    student_ID = input("Enter student ID for Student " + str(student_num) + ": ")
    student_num += 1
    print()
    askAgain = input("Enter another student? (y/n): ")
    if askAgain == 'n':
        x = False
        print()
        num_assignments = int(input("How many assignments were given: "))
    # assigning name to dictionary
    student_list[student_ID] = {
        'Name': student_name,
        'Scores': [],
    }
    # print out dictionarty
    for key in student_list:
        print("{}: {}".format(key,student_list[key]))
print()
print("Number of students: " + str(len(student_list)))

a = True
i = 0
j = 0
while i < len(student_list):
    avg_score = 0
    print()
    for key, Names in student_list.items():
        assignment_total = 0
        print()
        print("Please enter the scores for " + student_list[key]['Name'])
        currStudent = student_list[key]['Name']
        i += 1
        j = 0
        while j <= num_assignments:
            if j == num_assignments:
                break
            assignment= int(input("Enter score (0-100) for assignment " + str(j+1) + ": "))
            student_list[key]['Scores'].append(assignment)
            assignment_total = assignment_total + assignment
            avg_score = assignment_total / num_assignments
            j += 1
        print()
        print("Average score for {} is {:,.1f}".format(currStudent, avg_score))