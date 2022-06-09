from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField

# https://softwarekeep.com/help-center/how-to-fix-brightness-control-not-working-on-windows-10

class Subject(models.Model):
    title   = models.CharField(max_length = 200)
    slug    = models.SlugField(max_length = 200, unique=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Course(models.Model):
    owner   = models.ForeignKey(User, related_name = 'courses_created', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    title   = models.CharField(max_length=200)
    slug    = models.SlugField(max_length=200, unique=True)
    overview= models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Module(models.Model):
    course      = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)
    description = models.TextField(blank = True)
    order       = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)


class Content(models.Model):
    class Meta:
        ordering = ['order']

    module      = models.ForeignKey(Module, related_name='contents' , on_delete=models.CASCADE)
    order       = OrderField(blank=True, for_fields=['module'])
    content_type= models.ForeignKey(ContentType,
                                limit_choices_to = {'model__in':('text', 'video', 'image', 'file')},
                                on_delete=models.CASCADE)
    object_id   = models.PositiveIntegerField()
    item        = GenericForeignKey('content_type', 'object_id')



class ItemBase(models.Model):
    owner       = models.ForeignKey(User, related_name="%(class)s_related", on_delete=models.CASCADE)
    title       = models.CharField(max_length = 250)
    created     = models.DateTimeField(auto_now_add = True)
    updated     = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Text(ItemBase):
    content  = models.TextField()

class Image(ItemBase):
    file     = models.FileField(upload_to='images')

class File(ItemBase):
    file     = models.FileField(upload_to = 'file')

class Video(ItemBase):
    url      = models.URLField()
