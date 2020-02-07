from django.shortcuts import render


def we(request):
    return render(request=request,
                  template_name='main/iras.html')


