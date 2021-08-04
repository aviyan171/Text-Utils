from typing import ChainMap
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # a={"Name":"Abhiyan","LName":"Ureti"}
    return render(request,'index.html')
    # return HttpResponse("Hello <a href='/'>back</a>")

def analyze(request):
    #get the text
    dejtext=(request.POST.get("text","Default"))   #"GET" CAN ASLO BE USED BUT GET IS NOT SAFE
    removepunc=(request.POST.get("removepunc","off"))
    fullcaps=(request.POST.get("fullcaps","off"))
    Newlineremove=(request.POST.get("Newlineremove","off"))
    Removespace=(request.POST.get("Removespace","off"))
    Charactercount=(request.POST.get("Charactercount","off"))

    # analyzed=dejtext
    if removepunc=="on":
        punctuations='''!()-[];"%&*()_ '''
        analyzed=""
        for i in dejtext:
            if i not in punctuations:
                analyzed=analyzed+i

        params={'purpose':'Remove punctuations','analyzed_text':analyzed}
        dejtext=analyzed
        # return render(request,'analyze.html',params)
    
    if fullcaps=="on":
        analyzed=""
        for i in dejtext:
            analyzed=analyzed+i.upper()
        params={'purpose':'Change to Uppercase','analyzed_text':analyzed}
        dejtext=analyzed
        # return render(request,'analyze.html',params)

    if Newlineremove=="on":
        analyzed=""
        for i in dejtext:
            if i!="\n" and i!="\r":
                analyzed=analyzed+i
        params={'purpose':'Line removed','analyzed_text':analyzed}
        dejtext=analyzed
        # return render(request,'analyze.html',params)

    if Removespace=="on":
        analyzed=""
        for i in dejtext:
            if i!=" ":
                analyzed=analyzed+i
        params={'purpose':'Removed Space','analyzed_text':analyzed}
        dejtext=analyzed
        # return render(request,'analyze.html',params)

    if Charactercount=="on":
        analyzed=0
        for i in dejtext:
            analyzed=analyzed+1
        params={'purpose':'charatercount','analyzed_text':analyzed}
        dejtext=analyzed
        
    if (removepunc!="on" and fullcaps!="on" and Charactercount!="on" and Removespace!="on" and Newlineremove!='on'):
        return HttpResponse("error")


    return render(request,'analyze.html',params)
    



# def capfirst(request):
#     return HttpResponse("cap first")

# def newlineremove(request):
#     return HttpResponse("New line remove")
    
# def spaceremove(request):
#     return HttpResponse("Space remove")

# def charcount(request):
#     return HttpResponse("Charactercount")