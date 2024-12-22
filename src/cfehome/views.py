from django.shortcuts import render
from visits.models import PageVisit


def home(request):
    queryset = PageVisit.objects.all()
    title = "Home page"
    PageVisit.objects.create(path=request.path)

    context = {"title": title, "page_visit_count": queryset.count(),}
    return render(request, "cfehome/home.html", context)


def about_view(request):
    title = "About page"
    context = {"title": title}
    return render(request, "cfehome/about.html", context)