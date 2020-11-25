from django.shortcuts import render


def goodbye(request):
    return render(request, 'lmn/goodbye.html')

