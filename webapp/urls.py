from django.urls import path # type: ignore
from . import views


urlpatterns = [
    path('', views.landing_page, name="landing_page"),
    path('Guest/', views.student, name='student'),
    path('main/', views.main_page, name='main'),
    path('dtr/<int:pk>/', views.dtr_page, name='dtr'),
    path('attendance/', views.attendance_page, name='attendance'),
    path('history/', views.history_page, name='history'),
    path('dtrm/', views.dtrm, name="dtrm"),
    path('Add/', views.create_staff, name="addEmp"),
    path('register/', views.register, name='register'),
    path('orgchart/', views.org_chart, name = 'org_chart'),
    path('orgList/', views.org_List, name='orgList'),
    path('schedule/', views.schedule, name='schedule'),
    path('position/', views.position, name='position'),
    path('edit/<int:id>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
    path('', views.Logout, name='logout'),
    path('Employee/',views.UEmployee, name="userEmp"),
    path('Schedule/',views.UEmployeeSched, name="userEmpSched"),
    path('Admin/',views.AdminP, name='admin'),
    path('HomeView/', views.HomeView, name='home'),
    path('Details/<int:pk>', views.Details, name='details'),
    path('create/', views.createPost , name='createpost'),
    path('UserDtr/', views.Udtr, name='udtr'),
    path('Post/', views.Apost, name='Apost'),
    path('adminD/<int:pk>', views.adminDetails, name='admin-details'),
    # path('Admincreate/', views.adminCreatP , name='admincreatepost'),
    path('History/', views.copy_user_data_view, name='copy_user_data'),
    path('Ulogin/', views.Login, name='login'),
    path('studOrg/', views.studOrg, name='studorg'),
    path('Comlab/', views.comlabA, name='Acomlab'),
    path('comlab-admin/', views.comlabA, name='Acomlab'),  # Make sure this path matches
    path('Comlab-I/', views.comlabI, name='Icomlab'),
    path('user_data/', views.user_data, name='user_data'),
    path('Roles/', views.role_selection, name="roles"),
    path('Logout/', views.logout, name='Logout'),
] 