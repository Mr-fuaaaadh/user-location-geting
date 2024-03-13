from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserLocation

@login_required
def save_location(request):
    
    
    
    data = UserLocation.objects.all()    
    for i in data :
        
        print(i.user)
        print(i.longitude)
        print(i.latitude)
        print(i.timestamp)
        
        
        
        
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        UserLocation.objects.create(user=request.user, latitude=latitude, longitude=longitude)
        print('Location saved successfully')
        return render(request, 'save-location.html')
    else:
        print('Something else')
        return render(request, 'save-location.html')



def view_user_location(request, id):
    
    user_location = UserLocation.objects.filter(user=id).first()
    if user_location:
        user = user_location.user
        print(user)
        latitude = user_location.latitude
        longitude = user_location.longitude
        return render(request, 'user.html', {'latitude': latitude, 'longitude': longitude, 'user': user})
    else:
        return render(request, 'user.html', {'error': 'User location not found'})