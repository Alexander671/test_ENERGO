from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, 
                                            TokenVerifyView)

urlpatterns = [
    
    # admin
    path('admin/', admin.site.urls),

    path("accounts/", include("accounts.urls")),  
    
    # jwt auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # api   
    path('api/equations/', include('quadratic_equation.urls')),
    path('api/luftballons/', include('luftballons_99.urls')),
    
    
]
