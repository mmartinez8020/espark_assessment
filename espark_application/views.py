from django.shortcuts import render
from django.http import HttpResponse
import os
import csv
from utils import create_list, create_domain_dict,student_setup, update_values,real_function, create_html_table
import pandas as pd

def index(request):
    domain_order = open(os.path.join(os.path.dirname(__file__), 'csv/domain_order.csv')) 
    student_test = open(os.path.join(os.path.dirname(__file__), 'csv/student_tests.csv')) 
    student_test = create_list(student_test)
    domain_order = create_list(domain_order)
    domain_order = create_domain_dict(domain_order)
    print student_test
    student_list = student_setup(update_values(student_test))
    final = []
    for student in student_list:
        
        student_order = real_function(domain_order, student)
        final.append(student_order)
    html_table = create_html_table(final)
    context = {'myhtml': html_table}
    return render(request, 'index.html', context)
    

