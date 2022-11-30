from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('acconts/', include('django.contrib.auth.urls')),
    path('', include('catalog.urls'))
]
