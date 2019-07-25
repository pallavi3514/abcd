from myapp.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()
router.register(r'student',Studentvset,basename='student')
urlpatterns=router.urls