from django.urls import path
from . import views

urlpatterns = [
    # Home
    path("", views.index_view, name="home"),
    path("index/", views.index_view, name="index"),


    # Authentication
    path("register/", views.signup_view, name="signup"),
    path("reg/", views.reg, name="register_submit"),
    
    path("login/", views.signin_view, name="login"),
    path("log/", views.log, name="login_submit"),
    #path("register/submit/", views.reg, name="register_submit"),

    # Contact & Feedback
    path("contact/", views.contact_view, name="contact"),
    path('submit-contact/', views.submit_contact, name='submit_contact'),
    path("feedback/", views.feed_view, name="feedback"),
    path("subscribe/", views.sub, name="subscribe"),

    # Services
    path("service/", views.service_view, name="service_view"),
    path("service/book", views.book, name="book_service"),
    path("service/payment/", views.pay_view, name="service_payment"),
    path("service/payconfirm/", views.payt, name="pay_confirm"),

    # About Page
    path("about/", views.about_view, name="about"),

    # Payment Routes
    path("payment/", views.pay_view, name="payment"),
    path("payt/", views.payt, name="payment_process"),

    path("payment/confirm/", views.confirm, name="payment_confirm"),
     path('upi/', views.upi, name='upi'),
    path('callback/', views.callback, name='callback'),
    path('cod_success/', views.cod_success, name='cod_success'),
    path('option/', views.option, name='option'),
    path('sub/', views.sub, name='sub'),
]
