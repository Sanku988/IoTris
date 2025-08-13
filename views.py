from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from store.models import *
from django.conf import settings
import razorpay
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index_view(request):
    return render(request,'index.html')
def signup_view(request):
    return render(request,'register.html')
def reg(request):
    if request.method == 'POST':
        u=regist()
        u.fullname=request.POST['fullname']
        u.email=request.POST['email']
        u.password=request.POST['password']
        u.phone=request.POST['phone']
        u.confirm=request.POST['confirm']
        if u.password != u.confirm:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
        elif regist.objects.filter(email=u.email).exists():
            return render(request, 'register.html', {'error': 'Email already exists'})
        elif len(u.password) < 8:
            return render(request, 'register.html', {'error': 'Password must be at least 8 characters long'})
        elif not u.email.endswith('@gmail.com'):
            return render(request, 'register.html', {'error': 'Email must be a Gmail address'})
        elif not u.phone.isdigit() or len(u.phone) != 10:
            return render(request, 'register.html', {'error': 'Phone number must be 10 digits'})
        else:
            u.save()
            return redirect('login')
    return render(request, 'register.html')



def signin_view(request):
    return render(request,'login.html')
def log(request):
    if request.method == 'POST':
        u=regist()
        u.email=request.POST['email']
        u.password=request.POST['password']
        if regist.objects.filter(email=u.email, password=u.password).exists():
            return redirect('service_view')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
   
# feedback section
def feed_view(request):
    return render(request,'feedback.html')
def sub(request):
    if request.method == 'POST':
      u=feedback()
      u.name=request.POST['name']
      u.email=request.POST['email']
      u.message=request.POST['message']
      u.message2=request.POST['message2']
      u.rating=request.POST['rating']
      u.save()
    return render(request, 'feedbacksucess.html')
def feedback_confirm(request):
    return render(request, 'feedbacksucess.html')

    
# contact section
def contact_view(request):
    return render(request,'contact.html')
def submit_contact(request):
    if request.method == 'POST':
        u=subm()
        u.name=request.POST['name']
        u.email=request.POST['email']
        u.message=request.POST['message']
        u.save()
    return render(request, 'contactsucess.html')
def contact_confirm(request):
    return render(request, 'contactsucess.html')

def service_view(request):
    return render(request,'service.html')
def book(request):
    if request.method == 'POST':
        u=bookng()
        u.name=request.POST['name']
        u.phone=request.POST['phone']
        u.email=request.POST['email']
        u.service_type=request.POST['service_type']
        u.preferred_time=request.POST['preferred_time']
        u.address=request.POST['address']
        u.landmark=request.POST['landmark']
        u.notes=request.POST['notes']
        u.save()
    return redirect('option')
    
   

def about_view(request):
    return render(request,'about.html')


def pay_view(request):
    return render(request, 'payment.html')
def payt(request):
    if request.method == 'POST':
       u=pay()
       u.Card= request.POST['a1']
       u.number= request.POST['a2']
       u.EXP=request.POST['a3']
       u.cvv=request.POST['a4']
       u.save()
    return render(request, 'payconfirm.html')
def confirm(request):
    return render(request, 'payconfirm.html')

# Razorpay UPI Payment Integration
def upi(request):
    if request.method == "POST":
        amount = 50000  # in paise (INR 500)
        currency = 'INR'
        receipt = 'order_rcptid_11'
        notes = {'Shipping address': 'Mumbai, Maharashtra, India'}

        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        order = client.order.create({
            'amount': amount,
            'currency': currency,
            'receipt': receipt,
            'notes': notes,
            'payment_capture': 1
        })

        context = {
            'order_id': order['id'],
            'amount': amount,
            'razorpay_key': settings.RAZORPAY_KEY_ID
        }
        return render(request, "upi.html", context)
    return HttpResponse("Invalid request method", status=405)

@csrf_exempt
def callback(request):
    # You can add payment verification logic here if needed
    return render(request, "sucess.html")  # change to match your template name

def home(request):
    return render(request, "home.html")
def cod_success(request):
    return render(request, 'cod_success.html')
def option(request):
    return render(request, 'option.html')
