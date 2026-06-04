import json
def load_data():
    try:
        with open(r'data.json', 'r') as file:
            data = json.load(file)
            return data
    except Exception as e :
        if isinstance(e, FileNotFoundError):
            print("file not found")
            return []
        elif isinstance(e,json.JSONDecodeError):
            print(" file is empty or invalid structure")
            return []
        
def save_data(students):
    with open(r'data.json', 'w') as file:
        json.dump(students,file, indent=4)      
     