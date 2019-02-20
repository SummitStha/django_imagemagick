from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _
from django.conf import settings
import subprocess

class Book(models.Model):
    """Book class"""
    title = models.CharField(
        verbose_name = _(u'Title'),
        help_text = _(u'Commentary Title'),
        max_length = 255
    )
    slug = models.SlugField(
        verbose_name = _(u'Slug'),
        help_text = _(u'The unique uri component for this commentary'),
        max_length = 255,
        unique = True
    )
    document = models.FileField(
        verbose_name = _(u'The Book'),
        help_text = _(u'Upload a book document.'),
        upload_to = 'uploads/books/'
    )
    thumbnail = models.ImageField(
        verbose_name = _(u'Thumbnail'),
        help_text = _(u'The thumbnail'),
        upload_to = 'uploads/books/',
        blank = True, 
        null = True
    )

    def save(self):
        print('*******************************'*5, self.thumbnail)
        if self.thumbnail == None or self.thumbnail == '':
            thumbnail = "uploads/books/%s.jpg" % (self.slug,)
            self.thumbnail = thumbnail
            super(Book, self).save()
        else:
            super(Book, self).save()
    
    def __str__(self):
        return self.title

# What to do after a Book is saved
def book_post_save(sender, instance=False, **kwargs):
    """This post save function creates a thumbnail for the commentary Book"""
    book = Book.objects.get(pk=instance.pk)
    if instance.thumbnail == "uploads/books/%s.jpg" % (instance.slug,):
        command = "convert -quality 95 -thumbnail 255 %s%s[0] -flatten %s%s" % (settings.MEDIA_ROOT, book.document, settings.MEDIA_ROOT, book.thumbnail)

        proc = subprocess.Popen(command,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout_value = proc.communicate()[0]

# Hook up the signal
post_save.connect(book_post_save, sender=Book)
