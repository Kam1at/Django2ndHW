from django.shortcuts import render


def control(request):
    return render(request, 'ormnew/index.html')
