
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import UserProfile

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phonenumber = request.POST.get('mobile')
        address = request.POST.get('address')

        if not all([username, email, password, confirm_password]):
            messages.error(request, 'All fields are required')
            return render(request, 'registration.html')
        
        if password != confirm_password:
            messages.error(request, 'Password do not match')
            return render(request, 'registration.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return render(request, 'registration.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken')
            return render(request, 'registration.html')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        
        # Save additional fields in UserProfile
        UserProfile.objects.create(
            user=user,
            phone_number=phonenumber,
            address=address
        )
        login(request, user)
        return redirect('')  # Replace 'product_list' with the actual name of your URL pattern

    return render(request, 'registration.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not all([username, password]):
            messages.error(request, 'All fields are required')
            return render(request, 'login.html')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Login the user
            login(request, user)
            return redirect('/categories/')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
    
    return render(request, 'login.html')


    # Optionally, you can store additional information in a separate model or handle it here
    # Example:
    # UserProfile.objects.create(user=user, mobile=mobile, address=address)

    # # Log the user in after registration
    # login(request, user)

    # If you prefer to return a JSON response instead of a redirect:
    # return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    

    # def  register_user(request):
    #     if  request.method == 'POST':
    #         form = UserRegistrationForm(request.POST)
    #         if form.is_valid():
    #             user = form.save(commit=False)
    #             user.set_password(form.cleaned_data['password'])
    #             user.save()
    #             login(request, user)
    #             return redirect('product_list')  # Redirect to product list or any page after successful registration
    #     else:
    #         form = UserRegistrationForm()
    #     return render(request, 'registration.html', {'form': form})
