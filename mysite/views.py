from django.shortcuts import render_to_response


def home(request):
    return render_to_response('index.html')


def oops(request):
    return render_to_response('404.html')
