from django.urls import path
from . views import *
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
# from . import views as aboutview
from django.conf.urls import include


router = routers.DefaultRouter()
router.register('bio', BioViewSet)
router.register('timezoneworld', TimeZoneWorldViewSet)
router.register('ustimezone', UsTimeZoneViewSet)
router.register('russiatimezone', RussiaTimeZoneViewSet)
router.register('canadatimezone', CanadaTimeZoneViewSet)
router.register('dstcorrectionus', DstUsViewSet)
router.register('dstcorrectionrussia', DstRussiaViewSet)
router.register('dstcorrectioncanada', DstCanadaViewSet)



urlpatterns = [
    
    path('api/token/',
         jwt_views.TokenObtainPairView.as_view(),
         name ='token_obtain_pair'),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name ='token_refresh'),
    path('', include(router.urls)),
    
    
    ]



