
from django.urls import path
from . import views 


urlpatterns = [
    path('rooms/',views.RoomViewSet.as_view(),name='room-list'),
    path('rooms/<int:pk>/',views.roomDetailView.as_view(),name='room-detail'),
    path('rooms/create/',views.roomCreateView.as_view(),name='room-create'),
    path('rooms/<int:pk>/update/',views.roomUpdateView.as_view(),name='room-update'),
    path('rooms/<int:pk>/delete/',views.roomDeleteView.as_view(),name='room-delete'),
   
]