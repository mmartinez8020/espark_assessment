from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import os
import csv
from utils import create_list, create_domain_dict,student_setup, update_values, create_learning_path, create_html_table
import pandas as pd

def index(request):
    if request.method == 'POST':
        domain_order = request.FILES['domainorder']
        student_test = request.FILES['studenttests']
        student_test = create_list(student_test)
        domain_order = create_list(domain_order)
        domain_order = create_domain_dict(domain_order)
        student_list = student_setup(update_values(student_test))
        final = []
        for student in student_list:
            student_order = create_learning_path(domain_order, student)
            final.append(student_order)
        html_table = create_html_table(final)
        context = {'myhtml': html_table}
        return JsonResponse(context)
    return render(request, 'index.html')






    # domain_order = open(os.path.join(os.path.dirname(__file__), 'csv/domain_order.csv')) 
    # student_test = open(os.path.join(os.path.dirname(__file__), 'csv/student_tests.csv')) 
    # domain_test = open(os.path.join(os.path.dirname(__file__), 'csv/domain_order_test.csv'),'rU') 
    # test_file = open(os.path.join(os.path.dirname(__file__), 'csv/test_file.csv'),'rU') 
    # student_test = create_list(student_test)
    # domain_order = create_list(domain_order)
    # domain_order = create_domain_dict(domain_order)
    # student_list = student_setup(update_values(student_test))
    # final = []
    # for student in student_list:
    #     student_order = create_learning_path(domain_order, student)
    #     final.append(student_order)
    # html_table = create_html_table(final)
    # context = {'myhtml': html_table}
    # return render(request, 'index.html', context)
    
    



    # if request.method == 'POST':
    #     domain_order = request.FILES['domainorder']
    #     student_test = request.FILES['studenttests']
    #     student_test = create_list(student_test)
    #     domain_order = create_list(domain_order)
    #     domain_order = create_domain_dict(domain_order)
    #     student_list = student_setup(update_values(student_test))
    #     final = []
    #     for student in student_list:
    #         student_order = real_function(domain_order, student)
    #         final.append(student_order)
    #     print final            
    #     html_table = create_html_table(final)
    #     context = {'myhtml': html_table}
    #     print html_table
    #     return render(request, 'index.html',context)
    # return render(request, 'index.html')
    
