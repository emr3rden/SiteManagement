from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import LoginForm, RegisterForm, PersonnelCreateForm, ResidentCreateForm, ProblemForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
User = get_user_model()



def login_view(request):

    form = LoginForm(request.POST)

    if form.is_valid():

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        login(request, user)

        return redirect("homepage")

    return render(request, "admin/form.html", {"form": form, "title": "Giriş Yap"})



def logout_view(request):

    logout(request)

    return redirect("homepage")



def register_view(request):

    form = RegisterForm(request.POST)

    if form.is_valid():

        user = form.save(commit=False)
        password = form.cleaned_data.get("password1")
        user.set_password(password)
        user.is_staff = user.is_superuser = True
        user.save()
        # new_user = authenticate(email=user.email, password=password)
        # login(request, new_user)

        return redirect("homepage")

    return render(request, "admin/form.html", {"form": form, "title": "Üye Ol"})










def personnel_create(request):

    form = PersonnelCreateForm(request.POST)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password1")
        user.set_password(password)
        user.is_staff = user.is_superuser = True
        user.save()

        return redirect("homepage")

    return render(request, "admin/form.html", {"form": form, "title": "Üye Ol"})



def personnel_electric(request):

    if not request.user.is_authenticated:
        return HttpResponse('Bu sayfayı görüntülemeye yetkiniz yok!')

    personnel_list = User.objects.filter(username='Electric')

    paginator = Paginator(personnel_list, 3)

    page = request.GET.get('page')

    try:
        personnel = paginator.page(page)
    except PageNotAnInteger:
        personnel = paginator.page(1)
    except EmptyPage:
        personnel = paginator.page(paginator.num_pages)

    return render(request, 'personnel/personnel.html', {'personnel': personnel, })



def personnel_elevator(request):

    if not request.user.is_authenticated:
        return HttpResponse('Bu sayfayı görüntülemeye yetkiniz yok!')

    personnel_list = User.objects.filter(username='Elevator')

    paginator = Paginator(personnel_list, 3)

    page = request.GET.get('page')

    try:
        personnel = paginator.page(page)
    except PageNotAnInteger:
        personnel = paginator.page(1)
    except EmptyPage:
        personnel = paginator.page(paginator.num_pages)

    return render(request, 'personnel/personnel.html', {'personnel': personnel, })



def personnel_garden(request):

    if not request.user.is_authenticated:
        return HttpResponse('Bu sayfayı görüntülemeye yetkiniz yok!')

    personnel_list = User.objects.filter(username='Garden')

    paginator = Paginator(personnel_list, 3)

    page = request.GET.get('page')

    try:
        personnel = paginator.page(page)
    except PageNotAnInteger:
        personnel = paginator.page(1)
    except EmptyPage:
        personnel = paginator.page(paginator.num_pages)

    return render(request, 'personnel/personnel.html', {'personnel': personnel, })



def personnel_apartment(request):

    if not request.user.is_authenticated:
        return HttpResponse('Bu sayfayı görüntülemeye yetkiniz yok!')

    personnel_list = User.objects.filter(username='Apartment')

    paginator = Paginator(personnel_list, 3)

    page = request.GET.get('page')

    try:
        personnel = paginator.page(page)
    except PageNotAnInteger:
        personnel = paginator.page(1)
    except EmptyPage:
        personnel = paginator.page(paginator.num_pages)

    return render(request, 'personnel/personnel.html', {'personnel': personnel, })










def resident_create(request):

    form = ResidentCreateForm(request.POST)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password1")
        user.set_password(password)
        user.is_staff = user.is_superuser = True
        user.save()

        return redirect("homepage")

    return render(request, "admin/form.html", {"form": form, "title": "Üye Ol"})



def resident_host(request):

    if not request.user.is_authenticated:
        return HttpResponse('Bu sayfayı görüntülemeye yetkiniz yok!')

    resident_list = User.objects.filter(username='Host')

    paginator = Paginator(resident_list, 3)

    page = request.GET.get('page')

    try:
        resident = paginator.page(page)
    except PageNotAnInteger:
        resident = paginator.page(1)
    except EmptyPage:
        resident = paginator.page(paginator.num_pages)

    return render(request, 'resident/resident.html', {'resident': resident, })



def resident_tenant(request):

    if not request.user.is_authenticated:
        return HttpResponse('Bu sayfayı görüntülemeye yetkiniz yok!')

    resident_list = User.objects.filter(username='Tenant')

    paginator = Paginator(resident_list, 3)

    page = request.GET.get('page')

    try:
        resident = paginator.page(page)
    except PageNotAnInteger:
        resident = paginator.page(1)
    except EmptyPage:
        resident = paginator.page(paginator.num_pages)

    return render(request, 'resident/resident.html', {'resident': resident, })










def problem_create(request):

    if not request.user.is_authenticated:

        return HttpResponse('Bu sayfayı görüntülemeye yetkiniz yok!')

    form = ProblemForm(request.POST)

    if form.is_valid():

        Problems = form.save(commit=False)
        Problems.author = request.user
        Problems.save()

        return redirect('homepage')

    return render(request, 'problems/form.html', {'form': form, 'title': 'Sorun Ekle'})



def problem_resident(request):

    if not request.user.is_authenticated:

        return HttpResponse('Bu sayfayı görüntülemeye yetkiniz yok!')

    problems_list = Problems.objects.filter(author=request.user)

    paginator = Paginator(problems_list, 10)

    page = request.GET.get('page')

    try:
        problems = paginator.page(page)
    except PageNotAnInteger:
        problems = paginator.page(1)
    except EmptyPage:
        problems = paginator.page(paginator.num_pages)

    return render(request, 'problems/problems.html', {'problems': problems})



def problem_manager(request):

    if not request.user.is_authenticated:

        return HttpResponse('Bu sayfayı görüntülemeye yetkiniz yok!')

    problems_list = Problems.objects.all()

    paginator = Paginator(problems_list, 10)

    page = request.GET.get('page')

    try:
        problems = paginator.page(page)
    except PageNotAnInteger:
        problems = paginator.page(1)
    except EmptyPage:
        problems = paginator.page(paginator.num_pages)

    return render(request, 'problems/problems.html', {'problems': problems})



def problem_electric(request):

    if not request.user.is_authenticated:

        return HttpResponse('Bu sayfayı görüntülemeye yetkiniz yok!')

    problems_list = Problems.objects.filter(problem='Elektrik')

    paginator = Paginator(problems_list, 3)

    page = request.GET.get('page')

    try:
        problems = paginator.page(page)
    except PageNotAnInteger:
        problems = paginator.page(1)
    except EmptyPage:
        problems = paginator.page(paginator.num_pages)

    return render(request, 'problems/problems.html', {'problems': problems})



def problem_elevator(request):

    if not request.user.is_authenticated:

        return HttpResponse('Bu sayfayı görüntülemeye yetkiniz yok!')

    problems_list = Problems.objects.filter(problem='Asansör')

    paginator = Paginator(problems_list, 3)

    page = request.GET.get('page')

    try:
        problems = paginator.page(page)
    except PageNotAnInteger:
        problems = paginator.page(1)
    except EmptyPage:
        problems = paginator.page(paginator.num_pages)

    return render(request, 'problems/problems.html', {'problems': problems})



def problem_garden(request):

    if not request.user.is_authenticated:

        return HttpResponse('Bu sayfayı görüntülemeye yetkiniz yok!')

    problems_list = Problems.objects.filter(problem='Bahçe')

    paginator = Paginator(problems_list, 3)

    page = request.GET.get('page')

    try:
        problems = paginator.page(page)
    except PageNotAnInteger:
        problems = paginator.page(1)
    except EmptyPage:
        problems = paginator.page(paginator.num_pages)

    return render(request, 'problems/problems.html', {'problems': problems})



def problem_apartment(request):

    if not request.user.is_authenticated:

        return HttpResponse('Bu sayfayı görüntülemeye yetkiniz yok!')

    problems_list = Problems.objects.filter(problem='Bina')

    paginator = Paginator(problems_list, 3)

    page = request.GET.get('page')

    try:
        problems = paginator.page(page)
    except PageNotAnInteger:
        problems = paginator.page(1)
    except EmptyPage:
        problems = paginator.page(paginator.num_pages)

    return render(request, 'problems/problems.html', {'problems': problems})