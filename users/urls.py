from django.urls import path
from .views import *



urlpatterns = [

    path('login', login_view, name='login'),

    path('logout', logout_view, name='logout'),

    path('register', register_view, name='register'),

    path('personnel/create', personnel_create, name='personnel_create'),

    path('personnel/electric', personnel_electric, name='personnel_electric'),

    path('personnel/elevator', personnel_elevator, name='personnel_elevator'),

    path('personnel/garden', personnel_garden, name='personnel_garden'),

    path('personnel/apartment', personnel_apartment, name='personnel_apartment'),

    path('resident/create', resident_create, name='resident_create'),

    path('resident/host', resident_host, name='resident_host'),

    path('resident/tenant', resident_tenant, name='resident_tenant'),

    path('resident/problem/create', problem_create, name='problem_create'),

    path('resident/problems', problem_manager, name='problem_manager'),

    path('resident/myproblems', problem_resident, name='problem_resident'),

    path('resident/problem/electric', problem_electric, name='problem_electric'),

    path('resident/problem/elevator', problem_elevator, name='problem_elevator'),

    path('resident/problem/garden', problem_garden, name='problem_garden'),

    path('resident/problem/apartment', problem_apartment, name='problem_apartment'),

]
