import csv
import pandas as pd

def create_list(csvFile):
    csv_object = csv.reader(csvFile)
    list_of_lists = []
    try:
        for row in csv_object:
            list_of_lists.append(row)
    except:
        return "Not a csv"            
    return list_of_lists    

def create_domain_dict(domain_list):
    grades = {}
    for grade in domain_list:
        try:
          key = int(grade[0])
        except: 
          key = 0          
        values = grade[1:len(grade)]
        grades[key] = values
    return grades 

def update_values(student_list):
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
        print student
        print labels
        for i,j in zip(student, labels):
            if not str(i).isdigit() and len(i) > 1:
                name = j
                j = i
                i = name
            d.setdefault(i,[]).append(j)
        dict_students.append(d) 
    return dict_students  

def real_function(order, student_dict):
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