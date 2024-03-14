from gallery.models import Image
from gallery.serializers import ImagesSerializers
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsBetaUser, ReadOnly, IsBasicPlan, IsProPlan, IsPremiumPlan
from rest_framework import generics

# Create your views here.

class ImagesView(generics.ListAPIView ,generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImagesSerializers
    permission_classes = [IsAuthenticated, IsBetaUser | ReadOnly]
    
class GalleryView(generics.ListAPIView):
    serializer_class = ImagesSerializers
    permission_classes = [IsAuthenticated, IsPremiumPlan]
    def get_queryset(self):
        return Image.objects.filter(owner=self.request.user)
    
class ImagesBasicView(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImagesSerializers
    permission_classes = [IsAuthenticated, IsBasicPlan]
    def create_image(self, serializer):
        serializer.save(owner = self.request.user)
        
class ImagesProView(generics.CreateAPIView, generics.RetrieveUpdateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImagesSerializers
    permission_classes = [IsAuthenticated, IsProPlan]
    def create_image(self, serializer):
        serializer.save(owner = self.request.user)
    
    
class ImagesPremiumView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImagesSerializers
    permission_classes = [IsAuthenticated, IsPremiumPlan]
    def create_image(self, serializer):
        serializer.save(owner = self.request.user)