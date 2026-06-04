
def get_total_students(students):
    if len(students) == 0:
        return None
    else:
        total_no_of_student = len(students)
    #print("Total no.of students = " + total_no_of_student)
    return total_no_of_student




def get_average_percentage(students):
    total_percentage = 0
    for student in students:
        total_percentage=total_percentage+student["percentage"]

    average_percentage = total_percentage/len(students)

    return round(average_percentage,2)

def get_top_student(students):
    if len(students)==0:
        return None
    else:
        top_student = students[0]

        for student in students:
            if student["percentage"] > top_student["percentage"]:
                top_student = student
    return top_student

def get_lowest_student(students):
    if len(students)==0:
        return None
    else:
        lowest_student = students[0]
        for student in students:
            if student["percentage"] < lowest_student["percentage"]:
                lowest_student = student
    return lowest_student

def get_grade_distribution(students):
    
    grades = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }
    for student in students:
        grades[student["grade"]] += 1

    return grades

def student_statistics(students):
    if len(students) == 0:
        print("No student records available")
        return
    total_students= get_total_students(students)
    top_student = get_top_student(students)
    lowest_student = get_lowest_student(students)
    average_percentage = get_average_percentage(students)
    grade_distribution = get_grade_distribution(students)
    print("\n statistics \n")
    print("Total No.Of Students :" , total_students)
    print("Top percentage : " , top_student["percentage"])
    print("Top student : " , top_student["name"])
    print("lowest grade : " , lowest_student["percentage"])
    print("Lowest student : " , lowest_student["name"])
    print("Average percentage :" , average_percentage)
    #print("Grade distibution :" , grade_distribution)
    print("\nGrade Distribution")

    for grade, count in grade_distribution.items():
        print(f"{grade}: {count}")