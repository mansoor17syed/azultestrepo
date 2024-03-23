from django.shortcuts import render
from django.http import HttpResponse
from .models import currencydata    # currencydata is the model class defined in models.py
from .fetch_data import *


# Assuming the data to be entered is presnet in these lists


url_data_list = url_data()
cntry_name=url_data_list[0]
cntry_code=url_data_list[1]
cntry_crr=url_data_list[2]

def index(request, *args, **kwargs):
    # Iterate through all the data items
    for i in range(len(cntry_name)):

        # Insert in the database
        currencydata.objects.create(country_name = cntry_name[i], country_code = cntry_code[i], country_currency_value = cntry_crr[i])

    # Getting all the stuff from database
    query_results = currencydata.objects.all();

    # Creating a dictionary to pass as an argument
    context = { 'query_results' : query_results }

    # Returning the rendered html
    return render(request, "myapp/hello.html", context)
