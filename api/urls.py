from api.models import CourseResourse, CategoryResource
from tastypie.api import Api
from django.urls import path, include


api = Api(api_name='v1')
api.register(CourseResourse())
api.register(CategoryResource())

# For POST, DELETE add header
# Key: Authorization
# Value: ApiKey anatolij:dsfjh34234iujnjh43

urlpatterns = [
    path('', include(api.urls), name='index')
]
