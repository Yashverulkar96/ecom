
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),  
    path('categories/', include('product.urls')),       
    path('cart/', include('cart.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
