import pyrebase 
from django.shortcuts import render
from django.contrib import auth
import sys
from django.conf import settings
from django.conf.urls.static import static

config = {
"apiKey": "AIzaSyD7AmzNNojzPUcMXAqUR4wY_0QU8WLtS6U",
"authDomain": "cyberxs-hackathon-parking.firebaseapp.com",
"databaseURL": "https://cyberxs-hackathon-parking.firebaseio.com",
"projectId": "cyberxs-hackathon-parking",
"storageBucket": "",
"messagingSenderId": "336897760119",
"appId": "1:336897760119:web:2f7cad2393f7e211321f72"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
def singIn(request):
	return render(request, "signIn.html")

def postsign(request):
	email=request.POST.get('email')
	passw = request.POST.get("pass")
	try:
		user = authe.sign_in_with_email_and_password(email,passw)
	except:
		message = "invalid cerediantials"
		return render(request,"signIn.html",{"msg":message})
	print(user)
	session_id=user['localId']
	request.session['uid']=str(session_id)
	
	return render(request, "home.html",{"e":email})
	
def logout(request):
	auth.logout(request)
	
	return render(request,'signIn.html')
def signUp(request):

	return render(request,"signup.html")
	
def book(request):
	return render(request, "book.html")
	
def postbook(request):	
	days=request.POST.get("booking")
	days=int(days)
	pref=request.POST.get("prefrence")
	localid=request.session['uid']
	sapid = database.child('users').child(localid).child('details').child('sap').get().val()
	slots_date={}
	for day in range(days):
		dd="D"+str(day)
		slots_date[dd]=sapid
	print(localid)
	print(slots_date)
	data={"sapid":str(sapid),"Pref":str(pref),"slots":str(slots_date)}
	database.child("bookings").child(str(localid)).set(data)
	return render(request, "home.html",{"e":sapid})
	
def postsignup(request):
	name=request.POST.get('name')
	email=request.POST.get('email')
	passw=request.POST.get('pass')
	sap=request.POST.get('sap')
	phone=sap=request.POST.get('phone')
	pref=sap=request.POST.get('prefrence')
	elegible=1
	try:
		user=authe.create_user_with_email_and_password(email,passw)
		print(user)
		uid = user['localId']
		data={"sap":sap,"name":name,"email":email,"phone":phone,"pref":"","elegible":1}
		database.child("users").child(uid).child("details").set(data)
	except Exception as e:
		message=str(e)
		return render(request,"signup.html",{"messg":message})
	return render(request,"signIn.html")
	
def parking(request):
	print("in parlking loop")
	par=["P1","P2","P3"]
	slots=["A1","A2","A3","A4","A5","B1","B2","B3","B4","B5","C1","C2","C3","C4","C5"]
	for i in par:
		for slot in slots:
			data={'D1':'','D2':'','D3':'','D4':'','D5':'','D6':'','D7':'','D8':'','D9':'','D10':'','D11':'','D12':'','D13':'','D14':'','D15':'','D16':'','D17':'','D18':'','D19':'','D20':'','D21':'','D22':'','D23':'','D24':'','D25':'','D26':'','D27':'','D28':'','D29':'','D30':'','D31':'','D32':'','D33':'','D34':'','D35':'','D36':'','D37':'','D38':'','D39':'','D40':'','D41':'','D42':'','D43':'','D44':'','D45':'','D46':'','D47':'','D48':'','D49':'','D50':'','D51':'','D52':'','D53':'','D54':'','D55':'','D56':'','D57':'','D58':'','D59':'','D60':'','D61':'','D62':''}
			try:
				database.child("parking").child(i).child(slot).set(data)
			except Exception as e:
				message=str(e)
				return render(request,"signup.html",{"messg":message})	
	return render(request,"signIn.html")		