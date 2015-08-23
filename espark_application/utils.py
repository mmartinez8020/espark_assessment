import csv
import pandas as pd

def create_list(csvFile):
    """
    Returns a list of lists from a CSV file

    The function iterates though the csv object and appends each row to a list.
    If the csv_object is not iterable then a string "Not a csv" string is returned
    """
    csv_object = csv.reader(csvFile)
    list_of_lists = []
    try:
        for row in csv_object:
            list_of_lists.append(row)
    except:
        return "Not a csv"            
    return list_of_lists    

def create_domain_dict(domain_list):
    """
    Returns a dictionary with grades as keys and lists as values that contain the domain order

    The function iterates through the domain list and converts grades to integers
    and assigns a list of ordered domains to the correct grade level key.
    Incase of an Excel CSV, empty strings are removed.

    Example
    ----------

    >>> domain = [["K", "BL","HM","RR"], ["1","BL","HM","RR","L"],["2","R"]]
    
    {0: ['BL', 'HM', 'RR'], 1: ['BL', 'HM', 'RR', 'L'], 2: ['R']}
    """
    grades = {}
  
    for grade in domain_list:
        try:
            key = int(grade[0])
        except: 
            key = 0 
        values = grade[1:len(grade)]        
        removed_empty_strings = [domain for domain in values if domain]
        grades[key] = removed_empty_strings
    return grades 

def update_values(student_list):
    """
    Returns a new list where appropriate strings have been converted to integers

    The function iterates through student lists and checks for grade levels and converts them to 
    integers.
    """
    for student in student_list:
        for index, item in enumerate(student):
            if item.isdigit():
                student[index] = int(item)
            elif item == "K":
                student[index] = 0
    return student_list                               

def student_setup(students):
    labels = students[0]
    del students[0]
    dict_students = []
    for student in students:
        d = {}
        for i,j in zip(student, labels):
            if not str(i).isdigit() and len(i) > 1:
                name = j
                j = i
                i = name
            d.setdefault(i,[]).append(j)
        dict_students.append(d) 
    return dict_students




def create_learning_path(order, student_dict):
    student = []
    name = student_dict['Student Name'][0]
    del student_dict['Student Name'] 
    current_grade_level = min(student_dict)
    domain_check = student_dict[current_grade_level]
    if student_dict.keys()[0] == '':
        student_dict[0] = student_dict.pop('')
        current_level = 0
    while order.get(current_grade_level) != None and len(student) < 5:
        for domain in order[current_grade_level]:
            if domain in domain_check:
                grade = "K" if current_grade_level == 0 else current_grade_level
                student.append(str(grade) + "." + domain)
        current_grade_level += 1
        if student_dict.get(current_grade_level) != None:
            domain_check = student_dict[current_grade_level] + domain_check
        else:
            domain_check = domain_check
    student.insert(0,name)
    return student[0:6]            
        

def create_html_table(data):
    df_student = pd.DataFrame(data, columns= ["Names"] + [assign for assign in range(1,len(data[0]))])
    html_table = df_student.to_html(classes=["table", "table-striped", "table-condensed"], index=False)        
    return html_table
