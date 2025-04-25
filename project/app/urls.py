from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.ShowListView.as_view(),name='show_list'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('history/<int:pk>',views.HistoryView.as_view(),name='history'),
    path('history/',views.HistoryView.as_view(),name='history'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('remove/<int:pk>',views.RemoveView.as_view(),name='remove_show'),
    path('add/',views.AddView.as_view(),name='add_show'),
    path('admin_login/',views.AdminLoginView.as_view(),name='admin_login'),
    path('cancelbooking/<int:pk>',views.CancelBookingView.as_view(),name='cancel_booking'),   
]
