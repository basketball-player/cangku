from django.shortcuts import render


# Create your views here.
def index_page(request):
    return render(request, "index.html", locals())


def city_page(request):
    return render(request, "city.html", locals())
