from django.urls import path

from hello_django.calc import views

urlpatterns = [
    path('<int:A>/<int:B>', views.index.as_view(), name='calc'),
]