from django.shortcuts import render
from django.contrib.auth import authenticate

def home(request):
    if request.method == 'POST':
    	username = request.POST['username']
    	password = request.POST['password']
    	user = authenticate(username=username, password=password)

    	if user is not None:
		    # the password verified for the user
		    if user.is_active:
		        print("User is valid, active and authenticated")
		        return render(request, 'index.html', {"foo": "bar"},)        
		    else:
		        print("The password is valid, but the account has been disabled!")
    	else:
		    # the authentication system was unable to verify the username and password
		    print("The username and password were incorrect...!!")
    else:
    	return render(request, 'login.html', {"foo": "bar"},)

