
from django.contrib import admin
from django.urls import path, include
from events.views import send_email_api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('sendemail/', send_email_api),

]
