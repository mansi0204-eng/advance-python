from django.http import HttpResponse
from django.shortcuts import render, redirect

from .Services.Userservice import Userservice


def test(request):
    return HttpResponse("<h1>ORS!!!!</h1>")


def test_user_signup(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    login_id = request.POST.get('login_id')
    password = request.POST.get('password')
    Dob = request.POST.get('Dob')
    address = request.POST.get('address')
    csrfmiddlewaretoken = request.POST.get('csrfmiddlewaretoken')
    print(first_name)
    print(last_name)
    print(login_id)
    print(password)
    print(Dob)
    print(address)
    print(csrfmiddlewaretoken)
    return render(request, 'userregistration.html')


def user_signup(request):
    message = ''
    if request.method == "POST":
        param = {}
        param['first_name'] = request.POST.get('first_name')
        param['last_name'] = request.POST.get('last_name')
        param['login_id'] = request.POST.get('login_id')
        param['password'] = request.POST.get('password')
        param['Dob'] = request.POST.get('Dob')
        param['address'] = request.POST.get('address')
        service = Userservice()
        service.add(param)
    return render(request, 'UserRegistration.html', {'message': message})


def user_signin(request):
    message = ''
    if request.method == "POST":
        login_id = request.POST.get('login_id')
        password = request.POST.get('password')
        service = Userservice()
        user_data = service.auth(login_id, password)
        if len(user_data) != 0:
            request.session['first_name'] = user_data[0].get('first_name')
            return redirect('/ORS/welcome')
        else:
            message = 'LogIn Id and Password is invalid '
    return render(request, 'login.html', {'message': message})


def welcome(request):
    return render(request, 'welcome.html')


def logout(request):
    request.session['first_name'] = None
    return redirect('/ORS/signin')


def user_list(request):
    param = {}
    param['pageno'] = 1
    param['pagesize'] = 5

    if request.method == "POST":
        if request.POST['operation'] == "next":
            param['pageno'] = int(request.POST['pageno'])
            param['pageno'] += 1
        if request.POST['operation'] == "previous":
            param['pageno'] = int(request.POST['pageno'])
            param['pageno'] -= 1

    service = Userservice()
    list = service.search(param)
    return render(request, "userlist.html", {"list": list, 'pageno': param['pageno']})


def user_save(request):
    message = ''
    usr_data = [
        {}
    ]
    if request.method == "POST":
        param = {}
        param['first_name'] = request.POST.get('first_name')
        param['last_name'] = request.POST.get('last_name')
        param['login_id'] = request.POST.get('login_id')
        param['password'] = request.POST.get('password')
        param['Dob'] = request.POST.get('Dob')
        param['address'] = request.POST.get('address')
        service = Userservice()
        if request.POST['operation'] == "save":
            service.add(param)
            message = 'User Added Successfully'
        if request.POST['operation'] == "update":
            param['id'] = request.POST.get('id')
            service.update(param)
            usr_data = service.update(param)
            usr_data[0]['Dob'] = usr_data[0]['Dob'].strftime('%Y-%m-%d')
            message = 'User Updated Successfully'
    return render(request, 'User.html', {'form': usr_data[0], 'message': message})


def edit_user(request, id=0):
    service = Userservice()
    user_data = service.get(id)
    user_data[0]['Dob'] = user_data[0]['Dob'].strftime('%Y-%m-%d')
    return render(request, 'User.html', {'form': user_data[0]})


def delete_user(request, id=0):
    service = Userservice()
    service.delete(id)
    return redirect("/ORS/list/")
