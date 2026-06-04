def get_valid_integer(prompt):
    while True:
        try:
            valid_no = int(input(prompt))
            if valid_no > 0:
                return valid_no
            else:
                print("Enter a valid input")
        except ValueError:
            print("Enter a valid integer")

def get_valid_marks(subject):
    while True:
        try:
            mark = int(input("enter the mark for " + subject + " : "))  
            if 0 <= mark <= 100:
                return mark
            else :
                print ("enter a valid mark between 0 and 100") 
            
        except ValueError:
            print("enter a valid mark between 0 and 100") 

def get_yes_no(prompt):
    while True:
        yes_no = input(prompt)
        if yes_no.lower() == 'y' or yes_no.lower() == 'n':
            return yes_no
        else :
            print (prompt)
"""        
def get_valid_string(prompt):
    while True:
        name = input(prompt)
        if name.isalpha():
            return name
"""
def get_valid_string(prompt):
     while True:
        name = input(prompt)
        clean_name= name.replace(" ","")
        #if clean_name.isalpha():
        if len(clean_name) !=0:
             if clean_name.isalpha():
                return name
        else: 
            print ("Enter a valid string")

def get_valid_menu_option(prompt):
    while True:
        try:
            menu = int(input(prompt))
            if 0 < menu <= 7:  
                return menu
            else:
                print("Enter a valid menu option")
        except ValueError:
            print("Enter a valid integer")
