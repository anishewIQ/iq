__author__ = 'AivanF'
__copyright__ = 'Copyright 2019, IQ-Beat'
__contact__ = 'aivanf@iq-beat.com'

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exit', views.exit, name='exit'),
    path('departments', views.DepartmentsView.as_view(), name='department'),
    path('notifications', views.NotificationsView.as_view(), name='notifications'),

    path('dashboardcl', views.DashboardClView.as_view(), name='dashboardcl'),
    path('realtime', views.DashboardRealTimeView.as_view(), name='realtime'),
    path('acts', views.ActsView.as_view(), name='acts'),
    path('maps', views.MapsView.as_view(), name='maps'),
    path('upload/fcm', views.UploadFcmView.as_view(), name='upload-fcm'),

    #path('v1/', include('api.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
