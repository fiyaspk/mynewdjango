from django.urls import path,include
from.import views
urlpatterns = [
    path('test',views.testfn,name="test"),
    path('html',views.html)
]