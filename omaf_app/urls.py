from django.urls import path

from . import views


urlpatterns = [ 
        path("export/", views.export, name="csv"),
        path("download/", views.download, name="downloads")
        ]
