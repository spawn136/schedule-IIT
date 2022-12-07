from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
urlpatterns = [
    path('getScheduleView/<str:day>/<str:discipline>/<str:times>/<str:teacher>',
         views.GetScheduleView.as_view(), name="get"),
    path('setScheduleView/<str:day>/<str:discipline>/<str:times>/<str:teacher>',
         views.SetScheduleView.as_view(), name="set"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui")

]
