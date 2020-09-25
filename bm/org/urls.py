from django.urls import path
from.import views

urlpatterns =[
    path('',views.home,name='home'),
    path('login',views.login1,name="demo"),
    path('login2',views.login2,name="login2"),
    path('engreg',views.register,name="register"),
    path('farreg',views.farreg,name="farreg"),
    path('enter',views.fun,name="fun"),
    path('log',views.log,name="log"),
    path('log2',views.englogin,name="log2"),
    path('',views.contacts,name="contact"),
    path('signin',views.signup,name="signup"),
    path('farmer', views.farreg1, name="farreg"),
    path('signup',views.sign,name="sign"),
    path('hme',views.hme,name="hme"),
    path('backtohome',views.backtohome,name="back"),
    path('crop',views.crp,name="crp"),
    path('lgout',views.logout1,name="logout1"),
    path('logout',views.logout2,name="logout2"),
    path('cropreg',views.crop,name="cropreg"),
    path('question',views.farmerquiry,name="farmerquiry"),
    path('contact',views.contactus,name="cntct"),
    path('Farmerdetails',views.Farmerdetails,name='Farmerdetails'),
    path('Cropdetails',views.Cropdetails,name="cropdetails"),
    path('back',views.goback,name="goback"),
    path('back1',views.goback1,name="goback1"),
    path('bck',views.bck,name="bck"),
    path('bck2',views.bck2,name="bck2"),
    path('respond',views.respond,name="suggestion"),
    path('aboutcrops',views.aboutcrops,name="aboutcrops"),
    path('Farmer',views.Farmer,name="Farmer"),
    path('return',views.suggestion,name="suggestion"),
    path('aboutus',views.aboutus,name="aboutus")

]