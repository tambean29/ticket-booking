from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile 
from .models import Shows
from django.contrib.auth.models import User 
from datetime import datetime

class LoginView(View):
    def get(self, request):
        return render(request, 'Login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('show_list')
        return render(request, 'Login.html', {'error': 'Invalid credentials'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class HomeView(View):
    def get(self, request):
        shows = Shows.objects.all()
        return render(request, 'Home.html', {'shows': shows, 'user': request.user})

class RegisterView(View):
    def get(self, request):
        return render(request, 'Register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        is_admin = "is_admin" in request.POST
        UserProfile.objects.create(user=user, is_admin=is_admin)
        return redirect('login')

class HistoryView(View):
    def get(self, request,pk = None):
        history = request.session.get('history', [])
        if pk:
            show = Shows.objects.get(pk=pk)
            show_time_str = show.show_time.strftime('%H:%M:%S')
            show_date_str = show.show_date.strftime('%Y-%m-%d') 
            show_dict = {
                'id': show.id,
                'show_name': show.show_name,
                'show_time': show_time_str,
                'show_date': show_date_str,
                'available_seats': show.available_seats
            }
            if show_dict not in history:
                history.append(show_dict)
                request.session['history'] = history
              
        return render(request, 'History.html', {'history': history})

class ShowListView(View):
    def get(self, request):
        shows = Shows.objects.all()
        return render(request, 'ShowList.html', {'shows': shows, 'user': request.user})

class RemoveView(View):
    def get(self, request, pk):
        show = Shows.objects.get(pk=pk)
        show.delete()
        return redirect('show_list')

class AddView(View):
    def get(self, request):
        return render(request, 'AddShow.html')
    def post(self,request):
        name = request.POST.get('name')
        time = request.POST.get('time','').strip()
        time = datetime.strptime(time, "%H:%M").time()
        date = request.POST.get('date')
        available_seats = request.POST.get('available_seats')
        Shows.objects.create(show_name=name, show_time=time, show_date=date, available_seats=available_seats)
        return redirect('show_list')

class AdminLoginView(View):
    def get(self, request):
        return render(request, 'AdminLogin.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.userprofile.is_admin:
            login(request, user1)
            return redirect('show_list')
        return render(request, 'AdminLogin.html', {'error': 'Invalid credentials'})

class CancelBookingView(View):
    def get(self, request, pk):
        history = request.session.get('history', [])
        

        pk_to_remove = int(pk) 
        

        for show in list(history):
            if show['id'] == pk_to_remove:
                
                history.remove(show)
                item_removed = True
                break

        request.session['history'] = history
        

        return redirect('history')