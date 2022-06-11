from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from courses.views import CourseListView

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('course/', include('courses.urls', namespace='courses')),
    path('students/', include('students.urls', namespace='students')),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
