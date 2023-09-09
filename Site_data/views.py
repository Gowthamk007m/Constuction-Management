from django.shortcuts import render, redirect
from . models import *
# Create your views here.


def home_page(request):
    site_details = Site_User.objects.all()
    return render(request, 'pages/home.html', {'site_details': site_details})


def all_user(request):
    user=users.objects.all()
    return render(request, 'pages/one.html', {'user': user})


def add_site(request):
    site = Construction_Site.objects.all()
    return render(request, 'pages/individualsite.html', {'site': site})


def add_site_user(request):
    return render(request, 'pages/home.html')


def add_new_site(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        num_workers = request.POST.get('num_workers')
        budget = request.POST.get('budget')
        working_status = request.POST.get('working_status')
        location = request.POST.get('location')
        image = request.FILES.get('image')


        Construction_data = Construction_Site(name=name, num_workers=num_workers, budget=budget, image=image,
                                              location=location, working_status=working_status)
        Construction_data.save()

        return redirect('home')

    return render(request, 'pages/add_site.html')


def create_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        image = request.FILES.get('image')

        user = users(name=name, email=email, phone=phone, age=age, image=image)
        user.save()

        return redirect('home')

    # Render the form
    return render(request, 'pages/add_user.html')


def site_user_create(request):
    sites = Construction_Site.objects.all()
    user = users.objects.all()

    if request.method == 'POST':
        name_id = request.POST.get('name')
        site_role = request.POST.get('site_role')
        site_data_id = request.POST.get('site_data')

        site_user = Site_User(
            name_id=name_id, site_role=site_role, site_data_id=site_data_id)
        site_user.save()
        return redirect('/')

    return render(request,'pages/site_user.html',{'sites': sites, 'user': user})
