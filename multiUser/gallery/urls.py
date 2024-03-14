from django.urls import path, include
from gallery.views import GalleryView, ImagesBasicView, ImagesView, ImagesProView, ImagesPremiumView

urlpatterns = [
    path("images/<int:pk>", ImagesView.as_view(), name='images'),
    path("image-basic/", ImagesBasicView.as_view(), name="basic-plan"),
    path("image-pro/<int:pk>", ImagesProView.as_view(), name="pro-plan"),
    path("image-premium/", ImagesPremiumView.as_view(), name="premium-plan"),
    path("gallery/", GalleryView.as_view(), name='gallery')

]
