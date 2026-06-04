def calculate_total(marks):
    total = 0
    for values in marks.values():
        total = total + values
    return (total)

def calculate_percentage(total,no_of_subjects):

    
    percentage = total/no_of_subjects
    return(percentage)

def get_grade(percentage):
    grade=''
    percentage=round(percentage)
    if percentage > 90:
        grade = 'A'
    elif  75 < percentage <= 90 :
        grade = 'B'
    elif 60 < percentage <= 75 :
        grade = 'C'
    elif 45 < percentage <= 60 :
        grade = 'D'
    else :
        grade = 'F'
    return(grade)