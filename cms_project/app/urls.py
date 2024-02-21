from django.urls import path
from app.views import AuthorRegistrationView, AuthorLoginView,ContentListView, ContentDetailView

urlpatterns = [
    path('register/', AuthorRegistrationView.as_view(), name='register'),
    path('login/', AuthorLoginView.as_view(), name='login'),
    path('content/', ContentListView.as_view(), name='content-list'),
    path('content/<int:pk>/', ContentDetailView.as_view(), name='content-detail'),

]