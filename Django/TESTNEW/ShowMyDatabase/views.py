from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="16042006",
    database="quanlisanpham"
)


def getTable(request):
    cursor = db.cursor()
    cursor.execute('Select * from sanpham')
    tableData = cursor.fetchall()
    return render(request, 'readDatabase.html', {'tableData': tableData})

db.close()

