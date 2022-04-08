from django.urls import path

from body_measurments import views

app_name = 'body_measurements'

urlpatterns = [
    path('body_measurements_list/', views.BodyMeasurementsListView.as_view(), name = 'body_measurements_list'),
    path('body_measurements_detail/<pk>', views.BodyMeasurementsDetailView.as_view(), name='body_measurements_detail'),
    path('body_measurements_create/', views.BodyMeasurementsCreateView.as_view(), name='body_measurements_create'),
    path('body_measurements_update/<pk>', views.BodyMeasurementsUpdateView.as_view(), name='body_measurements_update'),
    path('body_measurements_delete/<pk>', views.BodyMeasurementsDeleteView.as_view(), name='body_measurements_delete'),
    path('body_measurements_chart/', views.BodyMeasurementsViewChart, name='body_measurements_chart'),
    path('body_measurements_get_chart/', views.BodyMeasurementsGetChart, name='body_measurements_get_chart'),
]