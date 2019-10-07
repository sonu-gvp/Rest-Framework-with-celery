from django.urls import path
from myapp import views
from myapp import newviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('generic_snippets/', views.RegisterList.as_view()),
    path('generic_snippets/<int:pk>/', views.RegisterDetail.as_view()),
    path('class_views/', newviews.RegisterList.as_view()),
    path('class_views/<int:pk>', newviews.RegisterDetail.as_view()),
     path('login', newviews.login),
    # path('user_list/', newviews.UserList.as_view()),
    # path('user_list/<int:pk>', newviews.UserDetail.as_view()),
    path('', views.show),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)