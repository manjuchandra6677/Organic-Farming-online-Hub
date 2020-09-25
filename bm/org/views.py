from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from.models import engineerregister
from.models import farmerregistration
from.models import cropregistration
from.models import farmerquiries
from.models import contact
from.models import typesofcrops
from django.contrib import messages
from django.core.mail import EmailMessage,send_mail
from django.conf import settings
global username
def home(request):

    return render(request,'home.html')

def login1(request):
    return render(request,'login.html')
def login2(self):
    return render(self,'login2.html')

def register(request):
    return render(request,'engreg.html')

def farreg(request):
    return render(request,'farreg.html')
def contacts(req):
    return render(req,'contactus.html')

def sign(self):
    return render(self,'signin.html')
def hme(self):
    return render(self,'home.html')
def backtohome(self):
    return render(self,'home.html')
def crp(self):
    return render(self,'cropreg.html')
def logout1(self):
    auth.logout(self)
    return render(self,'home.html')
def logout2(self):
    auth.logout(self)
    return render(self,'home.html')
def goback(self):
    return render(self,'engineer.html')
def goback1(self):
    return render(self,'engineer.html')
def bck(self):
    return render(self,'farm.html')
def bck2(self):
    return render(self,'engineer.html')
def respond(self):
    ids=self.POST['ids']
    email=self.POST['email']
    quiry=self.POST['quiry']
    qx=farmerquiries.objects.get(id=ids)
    qx.status="responded"
    qx.save()
    return render(self,'engineersuggestion.html',{'email':email,'quiry':quiry})
def aboutcrops(self):
    crop=typesofcrops.objects.all()
    return render(self,'aboutcrops.html',{'crops':crop})
def aboutus(self):
    return render(self,'aboutus.html')


def fun(self):
    global firstname
    global Name
    global gmailid
    if self.method == "POST":
        firstname = self.POST['firstname']
        Name=self.POST['Name']
        gender=self.POST['gender']
        date=self.POST['date']
        options=self.POST['options']
        enternumber=self.POST['enternumber']
        gmailid=self.POST['mailid']
        phonenumber=self.POST['phonenumber']

        eng=engineerregister(FirstName=firstname,LastName=Name,selectgender=gender,dateofbirth=date,
                             Qualification=options,
                             workexpierience=enternumber,emailid=gmailid,phonenumber=phonenumber)
        eng.save()


        return render(self, 'signin.html')

    else:
        return render(self, 'home.html')

def farreg1(req):
    global firstname
    global Name
    global gmailid
    if req.method=="POST":
        firstname=req.POST['firstname']
        Name=req.POST['Name']
        gender=req.POST['gender']
        date=req.POST['date']
        options=req.POST['options']
        idnumber=req.POST['idnumber']
        address=req.POST['address']
        pincode=req.POST['pincode']
        gmailid = req.POST['mailid']
        phonenumber=req.POST['phonenumber']

        farmer=farmerregistration(Name1=firstname,Name2=Name,gender=gender,date=date,options=options,idnumber=idnumber,address=address,
                                  pincode=pincode,mailid=gmailid,phonenumber=phonenumber)
        farmer.save()
        return render(req,'signin.html')
    else:
        return render(req,'home.html')

def signup(req):
    if req.method=="POST":

        user=req.POST['user']
        pass1=req.POST['pass1']
        pass2=req.POST['pass2']
        if User.objects.filter(username=user).exists():
            messages.info(req,"user exist")
            return render(req,'signin.html')
        else:
            if pass1==pass2:


                sign=User.objects.create_user(username=user,password=pass1,first_name=firstname,
                                              last_name=Name,email=gmailid)
                sign.save()
                return render(req,'home.html')
            else:

                messages.info(req,"password mismatch")
                return render(req,'signin.html')
    else:
        return render(req,'home.html')

def log(self):
    if self.method=="POST":
        username=self.POST['usr']
        password=self.POST['ps']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(self,user)
            return render(self,'farm.html')
        else:
            return render(self, 'signin.html')
    else:
        return render(self,'login.html')
def englogin(self):
    if self.method=="POST":
        username=self.POST['usr']
        password=self.POST['ps']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(self,user)
            return render(self,'engineer.html')
        else:
            return render(self,'signin.html')
    else:
        return render(self,'login2.html')

def crop(self):
    if self.method=="POST":
        id=self.POST['idnum']
        name=self.POST['nam']
        area=self.POST['are']
        soil=self.POST['options']
        start=self.POST['date1']
        end=self.POST['date2']
        irrigation=self.POST['irrigation']
        farming=self.POST['farming']

        crop=cropregistration(ids=id,name=name,area=area,soil=soil,start=start,end=end,
                               irrigation=irrigation,farming=farming)
        crop.save()
        return render(self,'farm.html')
    else:
        return render(self,'cropreg.html')
def farmerquiry(self):
    if self.method=='POST' and self.FILES['queryp']:
        fid=self.POST['fid']
        quiry=self.POST['text']
        fileup=self.FILES['queryp']
        status="not responded"

        quiry=farmerquiries(fid=fid,quiry=quiry,fileup=fileup,status=status)
        quiry.save()
        return render(self,'farm.html')
    else:
        return render(self,'home.html')

def contactus(self):
    if self.method=="POST":
        fname=self.POST['name1']
        sname=self.POST['name2']
        mail=self.POST['email']
        qstn=self.POST['quiry']
        cont=contact(firstname=fname,sname=sname,mail=mail,qstn=qstn)
        cont.save()
        return render(self,'home.html')
    else:
        return render(self,'contactus.html')
def Farmerdetails(request):
    farmer=farmerregistration.objects.all()
    return render(request,'farmerdetails.html',{'farmer':farmer})
def Cropdetails(self):
    crop=cropregistration.objects.all()
    return render(self,'cropdetails.html',{'crop':crop})

def Farmer(self):
    Farmer=farmerquiries.objects.all()
    return render(self,'getquiries.html',{'Farmer':Farmer})
def suggestion(self):
    if self.method=="POST":
        tomail = self.POST['mail']
        subject = self.POST["qry"]
        body = self.POST["subject"]
        to=[tomail]
        send_mail(subject, body, settings.EMAIL_HOST_USER, to)

        return render(self,'getquiries.html')
    else:
        return render(self,'engineer.html')




