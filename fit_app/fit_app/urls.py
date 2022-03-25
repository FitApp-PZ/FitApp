from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('calculators/', include('calculators.urls')),
    path('hydration/', include('hydration.urls')),
    path('activities/', include('activities.urls')),
    path('sleep/', include('sleep.urls')),
]
