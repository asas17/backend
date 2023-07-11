from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from diagnostico import views

#api versioning
routerDiagnostico = routers.DefaultRouter()
routerDiagnostico.register(r'diagnostico', views.DiagnosticoView, 'diagnostico')

urlpatterns = [
    path('docs/', include_docs_urls(title='Diagnostico Api')),
    path('api/v1/', include(routerDiagnostico.urls))
]