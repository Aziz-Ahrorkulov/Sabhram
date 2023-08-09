from django.urls import path    
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('users/', UserListCreateAPIView  .as_view(), name='user-list-create'),
    path('jobs/', JobListCreateAPIView  .as_view(), name='job-list-create'),
    path('jobs/<int:id>/', JobRetrieveUpdateAPIView.as_view(), name='job-retrieve-update'),
    path('applications/', ApplicationListCreateAPIView.as_view(), name='application-list-create'),
    path('api/applications/', application_list, name='application-list'),
    path('applications/<int:id>/', ApplicationRetrieveUpdateAPIView.as_view(), name='application-retrieve-update'),
    path('apply-to-next-manager/<int:application_id>/', apply_to_next_manager, name='apply-to-next-manager'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    

    path('login/', UserLoginAPIView.as_view(), name='user-login'),

]
    #query params:
    # is_hired = True/False
    # birth_range = 1990-2000
    # gender = male/female
    # first_name/last_name = STR
    # job = STR
