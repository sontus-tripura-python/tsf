from django.urls import path
from Leader_app import views

urlpatterns = [
  # path('', views.home, name='home'),
   path('leader/', views.branch_name, name='branch_name'),
   path('branch-form/', views.branch_form, name='branch_form'),
   path('branch-name/update/<int:pk>/', views.branch_name_update, name='branch_name_update'),
   path('branch-delete/<int:pk>/', views.branch_delete, name='branch_delete'),
   path('branch-year/<int:pk>/', views.branch_year, name='branch_year'),
   path('branch-year-form/<int:pk>/', views.branch_year_form, name='branch_year_form' ),
   path('branch-year/update/<int:pk>/', views.branch_year_update, name='branch_year_update'),
   path('branch-delete/<int:pk>', views.branch_year_delete, name='branch_year_delete'),
   path('branch-year/member/<int:pk>/', views.branch_member, name='branch_member'),
   path('add-member/<int:pk>/', views.add_member_form, name='add_member_form'),
    path('branch/<int:pk>/leader', views.branch_leader_details, name='branch_leader_details'),
    path('branch-member/delete/<int:pk>/', views.branch_member_delete, name='branch_member_delete'),
    path('branch-member-update/<int:pk>/', views.member_details_update, name='member_details_update'),
  # centralLeader
   path('central/year/', views.central_years, name='central_years'),
    path('central/year/create/', views.central_year_form, name='central_year_form'),
    path('central-year/update<int:pk>/', views.central_year_update, name='central_year_update'),
    path('central-year-delete/<int:pk>/', views.central_year_delete, name='central_year_delete'),
    path('central-member/create/<int:pk>/', views.central_member_form, name='central_member_form'),
    path('central-member/<int:pk>/update/', views.central_leader_update, name='central_leader_update'),
    path('central-member/<int:pk>/delete/', views.central_leader_delete, name='central_leader_delete'),
    path('central/year/<int:pk>/', views.central_leader, name='central_leader'),
    path('central/<int:pk>/', views.central_leader_details, name='central_leader_details'),

    # co-ordinators
        path('co-ordinator/', views.co_ordinator, name='co_ordinator'),
    path('co-ordinator/<int:pk>/', views.co_ordinator_details, name='co_ordinator_details'),
    path('co-ordinator/create/', views.coordinator_create, name='coordinator_create'),
    path('co-ordinator/update/<int:pk>', views.coordinator_update, name='coordinator_update'),
    path('co-ordinator/delete/<int:pk>/', views.co_ordinator_delete, name='co_ordinator_delete'),
]
