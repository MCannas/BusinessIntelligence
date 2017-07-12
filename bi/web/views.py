from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from .models import *
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.utils import timezone
from django.core.mail import send_mail, EmailMultiAlternatives
import MySQLdb
import json


def login(request):

    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")

        if len(username)>0:
            if len(password)>0:
	            user = authenticate(username=username, password=password)
	            if user is not None:
	                auth_login(request, user)
	                return redirect('home')

    return render(request, 'web/login.html')



def logout(request):

    auth_logout(request)
    return  redirect('login')


def home(request):

    if request.user.is_authenticated():
        user =  SystemUser.objects.filter(user_id=request.user)
        return render(request, 'web/home.html',{'user':user[0]})
    else:
        return redirect('login')
    

def createuser(request):

    if request.user.is_authenticated():
        userrolform = CreateUserRolForm()
        userform = CreateUserForm()
        user =  SystemUser.objects.filter(user_id=request.user)
        if request.method == "POST":
            userrolpost = CreateUserRolForm(request.POST)
            userpost = CreateUserForm(request.POST)
            print(userrolpost)
            print(userpost)
            if userpost.is_valid():
                saveuser=userpost.save(commit=False)
                user = User.objects.create_user(saveuser.email,saveuser.email,saveuser.password)
                user.first_name = saveuser.first_name
                user.last_name = saveuser.last_name
                user.save()
                if userrolpost.is_valid():
                    saveuserrol = userrolpost.save(commit=False)
                    saveuserrol.user = user
                    saveuserrol.save()
                    return redirect('home')
        return render(request, 'web/createuser.html',{'user':user[0],'userform':userform ,'userrolform':userrolform })
    else:
        return redirect('login')



def edituser(request):

    if request.user.is_authenticated():
        user =  SystemUser.objects.filter(user_id=request.user)
        users = SystemUser.objects.all()

        if request.method == "POST":
            userrolpost = CreateUserRolForm(request.POST)
            userpost = CreateUserForm(request.POST)
            if userpost.is_valid():
                    # SystemUser.objects.filter(user_first_name=iduser)
                # saveuser=userpost.save(commit=False)
                # user = User.objects.create_user(saveuser.email,saveuser.email,saveuser.password)
                # user.first_name = saveuser.first_name
                # user.last_name = saveuser.last_name
                # user.save()
                if userrolpost.is_valid():
                    # Products.objects.filter(id = idproduct).update(quantities = nextquantities)
                    # saveuserrol = userrolpost.save(commit=False)
                    # saveuserrol.user = user
                    # saveuserrol.save()
                    return redirect('home')


        if request.is_ajax():
            iduser = request.POST.get("iduser")
            userforedit = SystemUser.objects.filter(user_id=iduser)
            print(userforedit[0])
            userrolform = CreateUserRolForm(None,instance=userforedit[0])
            userform = CreateUserForm(None,instance=userforedit[0].user)
            return render(request, 'web/edituserform.html',{'user':user[0],'userform':userform,'userrolform':userrolform})
        return render(request, 'web/edituser.html',{'user':user[0],'users':users })
    else:
        return redirect('login')


def createconection(request):

    if request.user.is_authenticated():
        user =  SystemUser.objects.filter(user_id=request.user)
        connections = ConectionData.objects.all()

        if request.method == "POST":
            formconnection = CreateConnectionForm(request.POST)
            if formconnection.is_valid():
                formconnection.save()
                return redirect('home')
        if request.is_ajax():
            connectionform = CreateConnectionForm()
            return render(request, 'web/createconnectionform.html',{'connectionform':connectionform})

        return render(request, 'web/createconection.html',{'user':user[0],'connections':connections})
    else:
        return redirect('login')


def connectionlist(request):

    if request.user.is_authenticated():
        user =  SystemUser.objects.filter(user_id=request.user)
        connections = ConectionData.objects.all()
        if request.is_ajax():
            idconnection = request.POST.get("idconnection")
            connection = ConectionData.objects.filter(id=idconnection)        
            db = MySQLdb.connect(host=connection[0].host, user=connection[0].username, passwd=connection[0].password, db=connection[0].dbname)
            cur = db.cursor()
            cur.execute("SHOW TABLES")
            rows = cur.fetchall()
            tables = []
            for row in rows:
                for table in row:
                    tables.append(table)
            return HttpResponse(tables)
        return render(request, 'web/connectionlist.html',{'user':user[0],'connections':connections})
    else:
        return redirect('login')



def gettables(request):

    if request.user.is_authenticated():
        if request.is_ajax():
            idconnection = request.POST.get("idconnection")
            connection = ConectionData.objects.filter(id=idconnection)        
            db = MySQLdb.connect(host=connection[0].host, user=connection[0].username, passwd=connection[0].password, db=connection[0].dbname, port=int(connection[0].port))
            cur = db.cursor()
            cur.execute("SHOW TABLES")
            rows = cur.fetchall()
            tables = []
            for row in rows:
                item = {"table": "table"}
                for table in row:
                    item["name"] = table
                    tables.append(item)
            jsonData=json.dumps(tables)
            return HttpResponse(jsonData)

    else:
        return redirect('login')

def getsentences(request):

    if request.user.is_authenticated():
        if request.is_ajax():
            idconnection = request.POST.get("idconnection")
            connection = ConectionData.objects.filter(id=idconnection)
            sentences = serializers.serialize("json", Sentences.objects.filter(dbtype=connection[0].dbtype))
            return JsonResponse({'sentences':sentences})      
    else:
        return redirect('login')



#         

# db = MySQLdb.connect(host="localhost",    # your host, usually localhost
#                      user="john",         # your username
#                      passwd="megajonhy",  # your password
#                      db="jonhydb")        # name of the data base

# # you must create a Cursor object. It will let
# #  you execute all the queries you need
# cur = db.cursor()

# # Use all the SQL you like
# cur.execute("SELECT * FROM YOUR_TABLE_NAME")

# # print all the first cell of all the rows
# for row in cur.fetchall():
#     print row[0]

# db.close()