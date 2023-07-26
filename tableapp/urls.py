
from django.urls import path,include
from .views  import *


urlpatterns = [
    
    path('push/',push.as_view(),name='push'),
    path('view/',perview,name='view'),
    path('Edit_per/<int:id>/', Edit_per,name='edit'),
    path('del_per/<int:id>/', del_per,name='delete'),
    
    
    
]
