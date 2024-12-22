from django.urls import path
from visits import views

urlpatterns = [
    # path("", views.home, name="home"),
     path("", views.visits, name="visits"),
]
