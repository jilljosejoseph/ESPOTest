from django.shortcuts import render

def home(request):
    # Your code here!
    return render(request, "home.html")

# Feel free to make more views as needed