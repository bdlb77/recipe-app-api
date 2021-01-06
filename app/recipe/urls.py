from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views

# defaultRouter will generate routes for our views(recipe.views)

router = DefaultRouter()
router.register('tags', views.TagViewSet)

# for reverse() to look up url
app_name = 'recipe'


urlpatterns = [
    path('', include(router.urls))
]
