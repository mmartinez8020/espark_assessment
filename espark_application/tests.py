from django.test import TestCase
from utils import create_list, create_domain_dict,student_setup, update_values,real_function, create_html_table
import os
import csv
import pandas as pd

test_csv = open(os.path.join(os.path.dirname(__file__), 'csv/test_file.csv'),'rU') 
blank_csv = open(os.path.join(os.path.dirname(__file__), 'csv/blank_csv.csv'),'rU') 
pdf = open(os.path.join(os.path.dirname(__file__), 'csv/testpdf.pdf')) 
# domain_test = open(os.path.join(os.path.dirname(__file__), 'csv/domain_order_test.csv')) 

class UtilityFunctionsTestCase(TestCase):
    def test_create_list(self):
        test_list = create_list(test_csv)
        blank = create_list(blank_csv)
        pdf_file = create_list(pdf)
        self.assertEqual(len(test_list), 9)
        self.assertEqual(isinstance(test_list, list), True)
        self.assertEqual(len(blank), 0)
        self.assertEqual(isinstance(blank, list), True)
        self.assertEqual(pdf_file, 'Not a csv')

    def test_create_domain_dict(self):
        domain = [
          ["K", "BL","HM","RR"], 
          ["1","BL","HM","RR","L"],["2","R"]
        ]
        domain_result = create_domain_dict(domain)
        self.assertEqual(isinstance(domain_result, dict), True)
        self.assertEqual(domain_result[2], ["R"])
        self.assertEqual(len(domain_result), 3)

    def test_update_values(self):    
        student_grades = [
          ['Student Name', 'RF', 'RL', 'RI', 'L'], 
          ['Alex Trebek', '2', '3', 'K', '3'], 
          ['Sinbad', '3', 'K', '3', '3'],
          ['Mark Martinez', 'K', 'K', 'K', '2']
        ]
        update_student_grades = update_values(student_grades)
        print update_student_grades[3][1:]
        self.assertEqual(isinstance(update_student_grades, list), True)
        self.assertEqual(all(isinstance(item, int) for item in update_student_grades[3][1:]), True)

        

        