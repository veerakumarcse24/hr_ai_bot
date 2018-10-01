from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector

def hello(request):
	connection = mysql.connector.connect (host="localhost" ,user="root" ,passwd="" ,database="sample")
	query = connection.cursor ( )
	query.execute('SELECT name FROM student ORDER BY name')
	names = [row[0] for row in query.fetchall()]
	connection.close()
	return HttpResponse(names)
