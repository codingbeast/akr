from amazon import views
from django.urls import path

urlpatterns = [
    path("keyword-cloud/",views.keyword_cloud.as_view(),name="keyword_cloud")
]