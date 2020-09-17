# i have created this file - suarabh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'saurabh','place':'bangalore'}
    return render(request,'index.html',params)

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    if removepunc=='on':
        punctuations='''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params ={'purpose':'Removed Punctuation','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'changed to uppercase ', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if(newlineremover=='on'):
        analyzed=""
        for char in djtext:
            if char !='\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed new line', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)

    if(extraspaceremover == 'on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed extra spaces', 'analyzed_text': analyzed}


    if ( removepunc != 'on' and fullcaps!='on' and newlineremover!='on' and extraspaceremover!='on' ):
        analyzed=djtext
        params = {'purpose': 'Removed extra spaces', 'analyzed_text': analyzed}

    return render(request, 'analyze.html', params)




