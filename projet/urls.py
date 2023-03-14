from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('box.urls')),
    path('machines_laver/',include('Machines_à_laver.urls')),
    path('machines_secher/',include('Machines_à_sécher.urls'))
]
