from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    # Если вызван URL без относительного адреса (шаблон — пустые кавычки),
    # то вызывается view-функция index() из файла views.py
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
] 