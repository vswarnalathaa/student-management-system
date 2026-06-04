import json
import os
import calculations
import validation
import file_handler
import student_func
import statistic
subjects = ["Maths","English","Science","Social"]

def main():
    print("current working dir")
    print(os.getcwd())
    students = file_handler.load_data()
    while True:
        
        menu = validation.get_valid_menu_option("------------------\nStudent Management System\n-------------------\n1. Add student\n2. View all student\n3. Search student by ID\n4. Update student detail\n5. Delete student\n6. Staistics\n7. Exit\nEnter the option: ")
        if menu == 1:
            new_student = student_func.student_data(students)
            students.extend(new_student)
            for student in new_student:
                student_func.process_student(student)
            file_handler.save_data(students)
            
        elif menu == 2:
            student_func.display_all(students)
        elif menu == 3:
            s_id= validation.get_valid_integer("enter the ID to be searched : ")
            s=student_func.search_student(students,s_id)
            if s == None:
                print("student does not exist")  
            else:
                student_func.display_report(s)
        elif menu == 4:
            student_func.update_student(students)
        elif menu == 5:
            student_func.delete_student(students)
        elif menu == 6:
            statistic.student_statistics(students)
        else:
           break
   

    #print(os.getcwd())
    #print(total)
    #print(percentage)
    #print(grade)
    #print(student)



if __name__ == "__main__":
    main()