from django.shortcuts import render
from .models import Course
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView, DeleteView, CreateView, UpdareView


class ManageCourseListView(ListView):
    model = Course
    template_name = 'courses/manage/course/list.html'

class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(owner = self.request.user)

class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)

class OwnerCourseMixin(OwnerMixin):
    model = Course

class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy(manage_course_list)
    template_name = 'courses/manage/course/form.html'

class OwnerCourseListView(OwnerCourseMixin, ListView):
    template_name  = 'courses/manage/course/list.html'

class CourseCreateView(OwnerEditMixin, CreateView):
    pass

class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    pass

class CourseDeleteView(OwnerCourseMixin, DeleteView):
    success_url = reverse_lazy('manage_course_list')
    template_name = 'courses/manage/course/delete.html'
