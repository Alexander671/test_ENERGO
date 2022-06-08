from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    
    # api   
    path('api/equations/', include('quadratic_equation.urls')),
    path('api/luftballons/', include('luftballons_99.urls')),

    # auth
    path("accounts/", include("accounts.urls")),  
    
#     # jwt auth
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    
]
