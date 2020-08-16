from django.shortcuts import render, redirect
from .models import User, Person, Gift
from django.contrib import messages

# Create your views here.

def login_pg(request):
    request.session.clear()
    return render(request, 'app_one/login.html')

def register_pg(request):
    return render(request, 'app_one/register.html')

def main(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user' : user,
    }
    return render(request, 'app_one/main.html', context)

def register(request):
    if request.method == 'POST':
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = request.POST['password']
        )
    return redirect('/')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    results = User.objects.filter(email = email)
    if results:
        if results[0].password == password:
            request.session['user_id'] = results[0].id
            return redirect('/main')
        else:
            messages.error('Incorrect Email/Password')
            return redirect('/')
    else:
        messages.error('Incorrect Email/Password')
        return redirect('/')

def add_new_pg(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user' : user,
    }
    return render(request, 'app_one/add_new.html', context)

def all_people(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    user = User.objects.get(id=request.session['user_id'])
    

    context = {
        'user' : user,
    }
    return render(request, 'app_one/all_people.html', context)

def add_new(request):
    p_type = (request.POST['e_i'] + request.POST['s_n'] + request.POST['t_f'] + request.POST['p_j'])

    person = Person.objects.create(
        first_name= request.POST['first_name'],
        last_name= request.POST['last_name'],
        user= User.objects.get(id=request.session['user_id']),
        p_type=p_type
    )
    return redirect('/add_new_pg')

def select_person(request):
    person_id = request.POST['person']
    
    return redirect(f'/show_person/{person_id}')

def show_person(request, person_id):
    person = Person.objects.get(id=person_id)
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'person': person,
        'user' : user
    }

    return render(request, 'app_one/show_person.html', context)

def add_gift(request, person_id):
    person = Person.objects.get(id=person_id)
    Gift.objects.create(
        gift = request.POST['gift'],
        date_name = request.POST['date_name'],
        date = request.POST['date'],
        money = float(request.POST['money']),
        note = request.POST['note'],
        person = person
    )
    return redirect(f'/show_person/{person_id}')

def logout(request):
    request.session.clear()
    return redirect('/')