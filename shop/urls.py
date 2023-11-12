from django.contrib import admin
from django.urls import path
from store.views import index, product_detail
from accounts.views import signup, logout_user, login_user
from django.conf.urls.static import static

from shop import settings


urlpatterns = [
    path('', index, name='index'),
    path('admin/',admin.site.urls),
    path('signup/',signup,name="signup"),
    path('login/',login_user,name="login"),
    path('logout/',logout_user,name="logout"),
    path('product/<str:slug>/', product_detail, name="product"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
