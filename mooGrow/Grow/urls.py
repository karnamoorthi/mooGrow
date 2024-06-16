from django.urls import path
from Grow import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
	path('',views.index),
	path('msg',views.msg),
	path('login',views.login),
	path('order',views.order),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)