from django.test import TestCase
from utils import create_list, create_domain_dict,student_setup, update_values, create_learning_path, create_html_table
import os
import csv
import pandas as pd

test_csv = open(os.path.join(os.path.dirname(__file__), 'csv/test_file.csv'),'rU') 
blank_csv = open(os.path.join(os.path.dirname(__file__), 'csv/blank_csv.csv'),'rU') 
pdf = open(os.path.join(os.path.dirname(__file__), 'csv/testpdf.pdf')) 
domain_order = open(os.path.join(os.path.dirname(__file__), 'csv/domain_order.csv')) 
student_test = open(os.path.join(os.path.dirname(__file__), 'csv/student_tests.csv')) 
sample_solution = open(os.path.join(os.path.dirname(__file__), 'csv/sample_solution.csv')) 

class UtilityFunctionsTestCase(TestCase):
    def test_create_list(self):
        test_list = create_list(test_csv)
        blank = create_list(blank_csv)
        pdf_file = create_list(pdf)
        #Check if function returns correct length
        self.assertEqual(len(test_list), 9)
        #Check if function returns a list
        self.assertEqual(isinstance(test_list, list), True)
        #Check if function returns length of 0 is CSV is blank
        self.assertEqual(len(blank), 0)
        #Check if function returns a list
        self.assertEqual(isinstance(blank, list), True)
        #Check is correct string is returned when file is not a CSV
        self.assertEqual(pdf_file, 'Not a csv')

    def test_create_domain_dict(self):
        domain = [
          ["K", "BL","HM","RR"], 
          ["1","BL","HM","RR","L"],["2","R"]
        ]
        domain_result = create_domain_dict(domain)
        
        #Check if returns a dictionary
        self.assertEqual(isinstance(domain_result, dict), True)
        #Check if returns correcy key,value
        self.assertEqual(domain_result[2], ["R"])
        #Check if returns correct length of returned value
        self.assertEqual(len(domain_result), 3)

    def test_update_values(self):    
        student_grades = [
          ['Student Name', 'RF', 'RL', 'RI', 'L'], 
          ['Alex Trebek', '2', '3', 'K', '3'], 
          ['Sinbad', '3', 'K', '3', '3'],
          ['Mark Martinez', 'K', 'K', 'K', '2']
        ]
        update_student_grades = update_values(student_grades)
        
        #Check is output is a list
        self.assertEqual(isinstance(update_student_grades, list), True)
        #Check if all eligible items were converted to integers
        self.assertEqual(all(isinstance(item, int) for item in update_student_grades[3][1:]), True)

    def test_student_setup(self):
        student_results = [
          ['Student Name', 'Domain1', 'Domain2', 'Domain3', 'Domain4'], 
          ['Student 1', 2, 3, 0, 3], 
          ['Student 2', 3, 1, 1, 1] 
          ['Student 3', 0, 0, 1, 2], 
          ['Student 4', 2, 4, 4, 4], 
          ['Student 5', 2, 3, 0, 1], 
          ['Student 6', 4, 2, 1, 1], 
          ['Student 7', 5, 5, 0, 2], 
          ['Student 8', 0, 0, 4, 5]
        ]
        list_of_students = student_setup(student_results)
        print list_of_students
        #Check if output is a list
        self.assertEqual(isinstance(list_of_students, list), True)
        #Check if all items are dictionaries
        self.assertEqual(all(isinstance(student_dictionary, dict) for student_dictionary in list_of_students), True)

    def test_create_learning_path(self):
        solution_list = create_list(sample_solution)
        student_tests = create_list(student_test)
        domain_orders = create_list(domain_order)
        domain_order_dict = create_domain_dict(domain_orders)
        student_list_dict = student_setup(update_values(student_tests))
        #Check to see that all student results are in solution set 
        self.assertEqual(all(create_learning_path(domain_order_dict, student) in solution_list for student in student_list_dict), True)





        

        