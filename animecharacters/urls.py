from django.urls import path, include
from rest_framework import routers
from .views import Animecharacterviewset
# from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'animecharacters', Animecharacterviewset)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    # path('apitoken/',obtain_auth_token,name='obtain_token'),
]