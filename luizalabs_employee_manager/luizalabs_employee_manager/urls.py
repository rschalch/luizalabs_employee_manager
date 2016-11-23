
from django.conf.urls import url
from django.contrib import admin
from employees import views

urlpatterns = [
    url(r'', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^employee/$', views.EmployeeViewSet.as_view({'get': 'list'}),
        name='employee-list'),
]
