'''1.	Write a program to building a simple student grade management system for a class of students. The system will store student names and their grades (both as lists) and should be able to perform the following operations:
●	Add a new student and their grade.
●	Update the grade of an existing student.
●	Remove a student from the list.
●	Calculate and display the average grade of the class.
●	Display the highest and lowest grades in the class.
Tasks:
●	Use lists to store the student names and their corresponding grades.
●	Implement functions to add, update, remove, and calculate the average and extreme grades.'''


from unicodedata import name


student=[]
grades=[]
def add_student(name,grade):
    name=input("Enter student name: ")
    grades=float(input("Enter student grade: "))
    student.append(name)
    grades.append(grade)

def update_grade():
    name=input("enter student name to update grade:")
    if name in student:
        i=student.index(name)
        grades[i]=float(input("Enter new grade: "))
    else:
        print("Student not found.")

def remove_student():
    name=input("enter student name to remove:")
    if name in student:
        i=student.index(name)
        student.pop(i)
        grades.pop(i)
    else:
        print("Student not found.")
def average_grade():
    if len(grades) > 0:
        print("Average Grade =", sum(grades) / len(grades))
    else:
        print("No students")

def highest_lowest():
    if len(grades) > 0:
        print("Highest Grade =", max(grades))
        print("Lowest Grade =", min(grades))
    else:
        print("No students")

# Main Program
while True:
    print("\n1.Add")
    print("2.Update")
    print("3.Remove")
    print("4.Average")
    print("5.Highest & Lowest")
    print("6.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        update_grade()
    elif choice == 3:
        remove_student()
    elif choice == 4:
        average_grade()
    elif choice == 5:
        highest_lowest()
    elif choice == 6:
        break
    else:
        print("Invalid Choice")



