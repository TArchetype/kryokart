from django.contrib import admin
from django.urls import path, include

appname = "kryokart"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kryokart.urls'))
]