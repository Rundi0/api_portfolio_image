from django.conf.urls import include
from django.urls import path

from .views import CommentView, ImageListView, ImageView, PortfolioListView, PortfolioView, RootImageListView

urlpatterns = [
    path('portfolio/', PortfolioListView.as_view()),
    path('portfolio/<int:pk>', PortfolioView.as_view()),
    path('image/', ImageListView.as_view()),
    path('image/<int:pk>', ImageView.as_view()),
    path('', RootImageListView.as_view()),
    path('comment/', CommentView.as_view()),
]