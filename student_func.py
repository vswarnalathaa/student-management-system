import validation
import calculations
import file_handler

subjects = ["maths","english","science","social"]

def student_data(students):
    student_list = []
    while True :

        student = {}
        while True:
            student["id"] = validation.get_valid_integer("enter the student ID : ")
            id = search_student(students,student["id"])
            if id != None:
                print("student already exist")
            else:
                break
        
        student["name"]=validation.get_valid_string("enter the student name : ")
        student["marks"]={}
        for subject in subjects:

           # student["marks"][subject] = int(input(" enter the marks for the subject " + subject + " :"))
             student["marks"][subject] = validation.get_valid_marks(subject)
        student_list.append(student)
        print("Student added successfully")

        more_flag = validation.get_yes_no("do you want to enter more details(Y/N)")
        if more_flag == 'n' :
            break
    
    return(student_list)

def display_all(students):
    #print(type(student))
    for student in students:
        display_report(student)

def display_report(student):

    print("------------------------")
    print("Name:", student["name"])
    print("ID:", student["id"])
    print()

    print("Marks:")
    for subject, score in student["marks"].items():
        print(subject, ":", score)

    print()
    print("Total:", student["total"])
    print("Percentage:", student["percentage"])
    print("Grade:", student["grade"])
    print("------------------------")

def search_student(students,s_id):
    for student in students:
        if student["id"] == s_id:
            return student
    return None

def process_student(student):
    total= calculations.calculate_total(student["marks"])
    percentage = calculations.calculate_percentage(total,len(student["marks"]))
    grade =  calculations.get_grade(percentage)
    student["total"] =  total
    student["percentage"] = percentage
    student["grade"] = grade

def update_student(students):
    student_id = validation.get_valid_integer("enter the student ID to be updated : ")
    student=search_student(students,student_id)
    if student == None:
        print("student not found")
    else:
        subject = validation.get_valid_string("enter the subject for which marks need to be updated : ").lower()
        if subject not in subjects:
            print ("invalid subject")
            return
        else:
            student["marks"][subject] = validation.get_valid_marks(subject)
            print("Mark is updated for the subject " + subject )
            process_student(student)
    file_handler.save_data(students)
    print("Student updated successfully")

def delete_student(students):
    student_id = validation.get_valid_integer("enter the student ID to be updated : ")
    student=search_student(students,student_id)
    if student == None:
        print("student not found")
    else:
        students.remove(student)
        file_handler.save_data(students)
        print("Student deleted successfully")
