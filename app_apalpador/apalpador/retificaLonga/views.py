from django.shortcuts import render
from django.http import HttpResponse
import gspread

gc = gspread.service_account(filename='../../service_account.json')
sh = gc.open_by_key('1noVM0ci_yNDi7I2egsF2-erzuTgBLa9LrOrM4q96xCk')
worksheet = sh.worksheet("Página1")

# def media_data_input() :
#     received_values = {}
#     received_values = worksheet.get_all_records()
#     print(received_values)


# Create your views here.
def maq235(request):
    return render(request, "./retificaLonga/maq235.html")

def template(request):
    return render(request, "./retificaLonga/template.html")

def withtemplates(request):
    # return HttpResponse(worksheet.col_values(3)) retorna como string a coluna
    # return HttpResponse(worksheet.row_values(1)) retorna como string a linha 
    # return HttpResponse(worksheet.get_all_values()) retorna como lista 
    return HttpResponse(worksheet.get_all_records())