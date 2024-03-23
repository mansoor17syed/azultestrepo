from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import time
# Create your views here.

from .models import Student,currencydata    # Student is the model class defined in models.py

# Assuming the data to be entered is presnet in these lists


url = "https://api.coinbase.com/v2/exchange-rates"
response = requests.get(url)
data = response.json()
# print(data)
time.sleep(2)
print(data['data']['rates']['INR'])
time.sleep(2)
print(data['data']['rates']['SAR'])
time.sleep(2)
print(data['data']['rates']['CZK'])
time.sleep(2)
cntry_name = ['INDIA', 'SAUDI ARABIA','CZECH REPUBLIC']
cntry_code = ['INR', 'SAR','CZK']
cntry_crr_INR = data['data']['rates']['INR']
time.sleep(2)
cntry_crr_SAR = data['data']['rates']['SAR']
time.sleep(2)
cntry_crr_CZK = data['data']['rates']['CZK']
time.sleep(2)
cntry_crr=[cntry_crr_INR,cntry_crr_SAR,cntry_crr_CZK]
def index(request, *args, **kwargs):
    
    # Iterate through all the data items
    for i in range(len(cntry_name)):

        # Insert in the database
        # Student.objects.create(Name = stud_name[i], Age = stud_age[i], Marks = stud_marks[i])
        # Student.objects.create(student_name = stud_name[i], student_age = stud_age[i], student_marks = stud_marks[i])
        currencydata.objects.create(country_name = cntry_name[i], country_code = cntry_code[i], country_currency_value = cntry_crr[i])


    # Getting all the stuff from database
    query_results = currencydata.objects.all();

    # Creating a dictionary to pass as an argument
    context = { 'query_results' : query_results }

    # Returning the rendered html
    return render(request, "myapp/hello.html", context)
