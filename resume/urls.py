from django.urls import path
from .views import about, contact, works, resume

urlpatterns = [
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('works/', works, name='works'),
    path('resume/', resume, name='resume'),
]