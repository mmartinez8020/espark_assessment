import csv
import pandas as pd

def create_list(csvFile):
    """
    Returns a list of lists from a CSV file

    The function iterates though the csv object and appends each row to a list.
    If the csv_object is not iterable then a "Not a csv" statement is returned.
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
    Returns a dictionary with grades as keys and lists as values that contain the grade's domain order

    The function iterates through the domain list and converts grades to integers
    and assigns a list of ordered domains to the correct grade level key.
    Incase of an Excel CSV, empty strings are removed.

    Example
    -------

    domain = [["K", "BL", "HM", "RR"], ["1", "BL", "HM", "RR", "L"],["2", "R"]]
    
    >>> create_domain_dict(domain)
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
    Returns a new list where eligible strings have been converted to integers

    The function iterates through student lists and checks for grade levels and converts them to 
    integers. "K" is converted to 0.

    Example
    -------
    student_grades = [
          ['Student Name', 'RF', 'RL', 'RI', 'L'], 
          ['Alex Trebek', '2', '3', 'K', '3'], 
          ['Sinbad', '3', 'K', '3', '3'],
          ['Mark Martinez', 'K', 'K', 'K', '2']
        ]

    >>> update_values(student_grades)
    [['Student Name', 'RF', 'RL', 'RI', 'L'], ['Alex Trebek', 2, 3, 0, 3], ['Sinbad', 3, 0, 3, 3], ['Mark Martinez', 0, 0, 0, 2]]    
    """
    for student in student_list:
        for index, item in enumerate(student):
            if item.isdigit():
                student[index] = int(item)
            elif item == "K":
                student[index] = 0
    return student_list                               

def student_setup(students):
    """
    Returns a list of dictionaries corresponding to each student. The key to each
    dictionary corresponds to a grade level and the values are a list corresponding
    to the students required domain assignments per grade level.

    The function takes the list of students and iterates through the students.
    During iteration a dictionary is created with their grade levels as keys, domain levels within
    that grade level as lists. Each dictionary is appended to a list called dict_students. 
    Example
    -------
    student_results = [
          ['Student Name', 'Domain1', 'Domain2', 'Domain3', 'Domain4'], 
          ['Student 1', 2, 3, 0, 3], 
          ['Student 2', 3, 1, 1, 1], 
    ]

    >>> student_setup(student_results)
    [{0: ['Domain3'], 'Student Name': ['Student 1'], 3: ['Domain2', 'Domain4'], 2: ['Domain1']}, 
    {1: ['Domain2', 'Domain3', 'Domain4'], 'Student Name': ['Student 2'], 3: ['Domain1']}]

    """
    labels = students[0]
    del students[0]
    dict_students = []
    for student in students:
        d = {}
        for i,j in zip(student, labels):
            #Switches 'Student Name': ['Student 1'] to ['Student 1'] : 'Student Name'
            if not str(i).isdigit() and len(i) > 1:
                name = j
                j = i
                i = name
            d.setdefault(i,[]).append(j)
        dict_students.append(d) 
    return dict_students




def create_learning_path(order, student_dict):
    """
    Returns correct learning path given a student and a domain order.

    This function starts by grabbing the students name from the student_dict,
    reassigning it to the another variables (for use after ordering is complete), 
    and then deleting this key, value pair.

    The basic process of this function to create the correct ordering is as follows:
        - Obtain the students lowest grade level and the corresponding domain elements within this min level.
          Have these two components assigned to separate variables.
        - Next it creates a while loop. Inside this while loop  the function begins to iterate through the 
          order dictionary by starting at order[current_grade_level], where current_grade_level is the minimum grade 
          level for a student. As this iteration occurs, the function checks to see if the students testing level matches 
          an element in the order. If it does, append this lesson to the student lesson plan list.
        - Following this we increment our grade level and repeat the process.
        - The while loop is stopped when when the student list has reached a length of 5
          or if current_grade_level has incremented past the max grade in our order dictionary. 
          current_grade_level will surpass the max grade in our order dictionary when 
          a student 
    """
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
    student.insert(0,name)
    return student[0:6]            
        

def create_html_table(data):
    """
    Returns an html table with student lesson plans

    This function leverages pandas to transform a list of lists to an html table.
    """
    df_student = pd.DataFrame(data, columns= ["Names"] + [assign for assign in range(1,len(data[0]))])
    html_table = df_student.to_html(classes=["table", "table-striped", "table-condensed","table-nonfluid"], index=False)        
    return html_table
