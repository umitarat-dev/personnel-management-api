"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Three modules for swagger:
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator # Token kutusu için gerekli

# For Image urlpatterns:
from django.conf import settings
from django.conf.urls.static import static
from decouple import config # Çevre değişkenlerini okumak için

# Swagger arayüzüne 'Authorization' başlığı eklemek için Generator sınıfımız[cite: 2]
class JWTSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        # Şemaları ortam ayarlarına göre belirle[cite: 2]
        if settings.DEBUG:
            schema.schemes = ["http"]
        else:
            schema.schemes = ["https"]

        # Güvenlik tanımlamalarını ekle[cite: 2]
        schema.security_definitions = {
            'Token': {
                'type': 'apiKey',
                'name': 'Authorization',
                'in': 'header',
                # 'description': 'Token bazlı yetkilendirme için: Token <key>'
            }
        }
        schema.security = [{"Token": []}]
        return schema
    
schema_view = get_schema_view(
   openapi.Info(
      title="Personnel Management API",
      default_version='V.01',
      description="Personnel Management API with Docker & PostgreSQL integration, JWT Authentication, and Swagger Documentation",
      terms_of_service="#",
      contact=openapi.Contact(email="umitarat8098@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
   generator_class=JWTSchemaGenerator, # Hazırladığımız generator'ı buraya bağladık
)

# 1. Sabit URL Yolları (Her ortamda çalışır)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("api/", include("personnel.urls")),
    ]

# 2. Şartlı Swagger Yolları (Sadece ENV_NAME 'prod' değilse çalışır)
# Bu sayede PythonAnywhere'de 'dev' bırakırsan Swagger görünür, Docker'da 'prod' yaparsan gizlenir.
if config("ENV_NAME", default="dev") != "prod":
    urlpatterns += [
        path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
        path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    ]


# 3. Şartlı Debug Toolbar Yolları (Sadece DEBUG True ve uygulama yüklü ise)
# 'djdt' namespace hatasını bu kontrol sayesinde bir daha asla almazsın.
if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    
# 4. Media Dosyaları (Sadece Geliştirme Aşamasında)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    