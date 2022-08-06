from django.urls import path

from demo.api.views import UserDemoAPIView

urlpatterns = [
    path('data/', UserDemoAPIView.as_view(), name='user_demo_data'),
]
