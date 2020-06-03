#  I have created this file -Apoorv
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # f = open("C:/Users/Hp/Desktop/html1/About.html")
    # return HttpResponse('Home')
    return render(request, 'index.html')


def analyze(request):
    # Get the text

    flag = 0
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    # print(charcount)

    # Check which checkbox is on
    if removepunc == "on":
        flag=1
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == "on":
        flag = 1
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        flag = 1
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if newlineremover == "on":
        flag = 1
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

            else:
                print("no")
        print("pre", analyzed)
        djtext = analyzed
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if charcount == "on":
        analyzed = 0
        for var in djtext:
            if var != "":
                analyzed += 1
        if flag==1:
            params = {'purpose': 'Charcters Counted', 'analyzed_text':djtext+ '\n No of characters=' + str(analyzed)}
        else:
            params = {'purpose': 'Charcters Counted', 'analyzed_text': ' No of characters=' + str(analyzed)}
        return render(request, 'analyze.html', params)

    if removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on":
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

#
# def about(request):
#     return HttpResponse("hello APOORV")
#
#
# def removepunc(request):
#     # return HttpResponse("remove punc")
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     # Analyze the text
#     return HttpResponse("remove punc")
#
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
#
# def newlineremove(request):
#     return HttpResponse("capitalize first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover")
#
#
# def charcount(request):
#     return HttpResponse("charcount ")
# if (removepunc or extraspaceremover or newlineremover or fullcaps) == 'on':
#     params = {'purpose': 'Charcters Counted', 'analyzed_text': djtext + ' No of characters=' + str(analyzed)}
# else:
#     params = {'purpose': 'Charcters Counted', 'analyzed_text': ' No of characters=' + str(analyzed)}