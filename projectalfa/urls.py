
from django.contrib import admin
from django.urls import path,include
from main import urls as mainurls
from amazon import urls as amazonurls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(mainurls)),
    path('',include(amazonurls))
]
