from django.shortcuts import render, redirect
from django.contrib import messages
from django.middleware.csrf import get_token
from django.templatetags.static import static
from .models import User

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        userType = request.POST.get('userType')

        if not all([email, password, userType]):
            messages.error(request, 'All fields are required.')
            return redirect('login')

        try:
            user = User.objects.get(email=email, userType=userType)
            if user.password == password:  # Note: In production, use hashed passwords
                request.session['currentUser'] = {
                    'id': user.id,
                    'email': user.email,
                    'userType': user.userType,
                    'subject': user.subject,
                }
                # Redirect based on user type
                if userType == 'admin':
                    return redirect('/admin_home/')
                elif userType == 'trainer':
                    subject = user.subject
                    if subject == 'js':
                        return redirect('/js_trainer/')
                    elif subject == 'css':
                        return redirect('/css_trainer/')
                    elif subject == 'java':
                        return redirect('/java/')
                    elif subject == 'python':
                        return redirect('/python/')
                    else:
                        return redirect('/subject_trainer/')
                elif userType == 'trainee':
                    return redirect('/student_home/')
            else:
                messages.error(request, 'Invalid password.')
        except User.DoesNotExist:
            messages.error(request, 'User not found.')

        return redirect('login')

    return render(request, 'login.html')

def admin_home(request):
    return render(request, 'admin_home.html')

def student_home(request):
    return render(request, 'student_home.html')

def js_trainer(request):
    return render(request, 'js_trainer.html')

def css_trainer(request):
    return render(request, 'css_trainer.html')

def java_trainer(request):
    return render(request, 'java.html')

def python_trainer(request):
    return render(request, 'Python.html')

def subject_trainer(request):
    return render(request, 'subject_trainer.html')

def admin_profile(request):
    return render(request, 'admin_profile.html')

def registration(request):
    if request.method == 'POST':
        fullName = request.POST.get('fullName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        phone = request.POST.get('phone')
        userType = request.POST.get('userType')
        subject = request.POST.get('subject')

        if not all([fullName, email, password, confirmPassword, phone, userType]):
            messages.error(request, 'All fields are required.')
            return redirect('registration')

        if password != confirmPassword:
            messages.error(request, 'Passwords do not match.')
            return redirect('registration')

        if userType == 'trainer' and not subject:
            messages.error(request, 'Subject is required for trainers.')
            return redirect('registration')

        try:
            user = User.objects.create(
                email=email,
                password=password,  # Note: In production, hash the password
                userType=userType,
                subject=subject if userType == 'trainer' else None
            )
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
        except Exception as e:
            messages.error(request, 'Registration failed. Email may already exist.')
            return redirect('registration')

    return render(request, 'registration.html')

# Add more views for other pages as needed
