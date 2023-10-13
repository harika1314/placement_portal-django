"""firstproject URL Configuration

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
from django.urls import path
from firstapp.views import home,placements,mocktest,submit,tests,footer,press,checkEligibility,cgpaa,contact
from django.conf.urls.static import static
from django.conf import  settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path('placements',placements,name="placements"),
    path('mocktest',mocktest,name="mocktest"),
    path("submit",submit,name="submit"),
    path("tests",tests,name="tests"),
    path("footer",footer,name="footer"),
    path("press",press,name="press"),
    path("checkEligibility",checkEligibility,name="checkEligibility"),
    path("cgpaa",cgpaa,name="cgpaa"),
    path("contact",contact,name="contact"),
  
]

    
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

