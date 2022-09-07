from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import*
# Create your views here.


# @login_required(login_url='login')
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'ud/login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('home')


def index(request):
    document = NOTICE.objects.all().order_by("-created")
    context = {'document': document}

    return render(request, 'ud/index.html', context)

    # return render(request, 'ud/index.html', context)


def Contact(request):
    document = CONTACT.objects.all().order_by("-created")
    context = {'document': document}
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        subject = request.POST.get('subject')
        detail = request.POST.get('detail')
        contact = CONTACT(name=name, phone_number=phone_number,
                          email=email, subject=subject, detail=detail)

        if contact.email[:8] == "2019ugmm" or contact.email[:8] == "2019UGMM" and contact.email[12:] == "nitjsr.ac.in" or contact.email[12:] == "NITJSR.AC.IN":
            contact.save()
            html_content = f'''
                <div style="font-family: Helvetica,Arial,sans-serif;min-width:1000px;overflow:auto;line-height:2">
                    <div style="margin:50px auto;width:80%;padding:20px 0">
                        <div style="border-bottom:1px solid #eee">
                        <a href="" style="font-size:1.4em;color: #46c894;text-decoration:none;font-weight:600">T&P CELL</a>
                        </div>
                        <p style="font-size:1.1em">Hi, i am {contact.name}  .</p>
                        <p>My email id is {contact.email} . </p>
                        <p>I have contacted you regarding {contact.subject} .</p>
                        <h3>Query</h3>
                        <p>{contact.detail}.</p>

                        <p style="font-size:0.9em;">Thank You</p>
                        <hr style="border:none;border-top:1.5px solid #eee" />
                    </div>
                </div>
                '''
            mail = EmailMessage(
                'T&P Cell',
                html_content,
                None,
                ['utkarshdeep635@gmail.com'],

            )
            mail.content_subtype = "html"
            mail.send()

        return render(request, 'ud/contact.html', context)
    else:
        return render(request, 'ud/contact.html', context)


def Resume(request):
    document = RESUME.objects.all().order_by("-created", "-email")
    context = {'document': document}
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        resume = request.FILES['resume']
        Resume_ = RESUME(name=name,
                         email=email,  resume=resume)
        if Resume_.email[:8] == "2019ugmm" or Resume_.email[:8] == "2019UGMM" and Resume_.email[12:] == "nitjsr.ac.in" or Resume_.email[12:] == "NITJSR.AC.IN":
            Resume_.save()
            html_content = f'''
                <div style="font-family: Helvetica,Arial,sans-serif;min-width:1000px;overflow:auto;line-height:2">
                    <div style="margin:50px auto;width:80%;padding:20px 0">
                        <div style="border-bottom:1px solid #eee">
                        <a href="" style="font-size:1.4em;color: #46c894;text-decoration:none;font-weight:600">T&P CELL</a>
                        </div>
                        <p style="font-size:1.1em">Hi, i am {Resume_.name}  .</p>
                        <p>My email id is {Resume_.email} . </p>
                        <p>I have uploaded my resume  .</p>
                        
                        <p>{Resume_.resume}.</p>

                        <p style="font-size:0.9em;">Thank You</p>
                        <hr style="border:none;border-top:1.5px solid #eee" />
                    </div>
                </div>
                '''
            mail = EmailMessage(
                'T&P Cell',
                html_content,
                None,
                ['utkarshdeep635@gmail.com', '2019UGMM088@NITJSR.AC.IN'],

            )
            mail.content_subtype = "html"
            mail.send()

        return render(request, 'ud/resume.html', context)
    else:
        messages.success(
            request, 'Your institute email id')
        return render(request, 'ud/resume.html', context)


def Notice(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        text = request.POST.get('text')
        notice = request.FILES['notice']
        Notice_ = NOTICE(subject=subject, text=text,
                         notice=notice)
        Notice_.save()
    document = NOTICE.objects.all().order_by("-created")
    context = {'document': document}
    return render(request, 'ud/notice.html', context)


def Pyqs(request):
    if request.method == "POST":
        company = request.POST.get('company')
        note = request.POST.get('note')
        question = request.FILES['question']
        PYQs_ = PYQS(company=company, note=note,
                     question=question)
        PYQs_.save()
    document = PYQS.objects.all().order_by('-created')
    context = {'document': document}
    return render(request, 'ud/pyqs.html', context)


def about(request):

    return render(request, 'ud/about-us.html')


# def NoticeList(request):
#     document = NOTICE.objects.all().order_by("-created")
#     context = {'document': document}
#     return render(request, 'ud/index.html', context)


@login_required(login_url='login')
def ContactedList(request):
    List = CONTACT.objects.all().order_by("-created")
    context = {'List': List}
    return render(request, 'ud/contactlist.html', context)


@login_required(login_url='login')
def ResumeList(request):
    List = Resume.objects.all().order_by("-created")
    context = {'List': List}
    return render(request, 'ud/resumelist.html', context)
