from django.db import models
from tinymce import HTMLField
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
from tinymce import HTMLField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Upload(models.Model):

    title = models.CharField(max_length=20)




    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    #content = HTMLField()
    # comment_count = models.IntegerField(default = 0)
    # view_count = models.IntegerField(default = 0)
    upload = models.ManyToManyField(Upload)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(max_length=100)
    uploa = models.ImageField(upload_to='uploads',default = 0)
    uplod = models.ImageField(upload_to='uploads',default = 0)
    uplad = models.ImageField(upload_to='uploads',default = 0)
    uplodd = models.ImageField(upload_to='uploads',default = 0)
    
    upoad = models.ImageField(upload_to='uploads',default = 0)
    uload = models.ImageField(upload_to='uploads',default = 0)
    pload = models.ImageField(upload_to='uploads',default = 0)
    uploa = models.ImageField(upload_to='uploads',default = 0)
 
    uplo = models.ImageField(upload_to='uploads',default = 0)
    upld = models.ImageField(upload_to='uploads',default = 0)
    upad = models.ImageField(upload_to='uploads',default = 0)
    uoad = models.ImageField(upload_to='uploads',default = 0)

    upla = models.ImageField(upload_to='uploads',default = 0)
    uplb = models.ImageField(upload_to='uploads',default = 0)
    upac = models.ImageField(upload_to='uploads',default = 0)
    uoed = models.ImageField(upload_to='uploads',default = 0)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={
            'id': self.id
        })

    def get_update_url(self):
        return reverse('event-update', kwargs={
            'pk': self.pk
        })

    def get_delete_url(self):
        return reverse('event-delete', kwargs={
            'pk': self.pk
        })
    
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def comment_count(self):
        return Comment.objects.filter(event=self).count()

    @property
    def view_count(self):
        return eventView.objects.filter(event=self).count()


class Events(models.Model):
    name_event = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='pics')    
class Blog(models.Model):
    name_blog = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='pics')
    author = models.CharField(max_length=255)
    date = models.DateTimeField()

