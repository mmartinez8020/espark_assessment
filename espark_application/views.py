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
        student_test_list = create_list(student_test)
        domain_order_list = create_list(domain_order)
        domain_order = create_domain_dict(domain_order_list)
        student_list = student_setup(update_values(student_test_list))
        student_learning_paths = []
        for student in student_list:
            student_order = create_learning_path(domain_order, student)
            student_learning_paths.append(student_order)
        html_table = create_html_table(student_learning_paths)
        context = {'myhtml': html_table}
        return JsonResponse(context)
    return render(request, 'index.html')
  
  
