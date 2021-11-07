from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clients_api.views import ClientsViewSet, ClientesPorSexo, ClientesPorEstado, ClientesPorCpf

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Client data provider",
      terms_of_service="#",
      contact=openapi.Contact(email="ulyssesdmnt@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()

router.register('clients', ClientsViewSet, basename='Clients')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('clients/gender_filter/<str:gender>', ClientesPorSexo.as_view()),
    path('clients/state_filter/<str:state>', ClientesPorEstado.as_view()),
    path('clients/cpf_filter/<str:cpf>', ClientesPorCpf.as_view()),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
