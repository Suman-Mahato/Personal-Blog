from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home/home.html')
    #return HttpResponse('This is home page')

def about(request):
    return render(request, 'home/about.html')

def post(request):
    return render(request, 'home/post.html')

def gallery(request):
    return render(request, 'home/gallery.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']     

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been sucessfully sent")
    return render(request, 'home/contact.html')


def search(request):
    return render(request, 'home/search.html', parms)  