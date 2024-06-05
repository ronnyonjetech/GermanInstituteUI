from django.urls import path
from . import views

urlpatterns = [
   path('menschenA1/', views.menschen_a1, name='menschen_a1pdf'),
   path('menschenA2/', views.menschen_a2, name='menschen_a2pdf'),
   path('menschenB1/', views.menschen_b1, name='menschen_b1pdf'),
   path('Grammatik_Aktiv/', views.Grammatik_Aktiv, name='Grammatik_Aktivpdf'),
   path('landing/', views.landing, name='landing'),
]
