# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


MAX_DIGEST_LEN = 300
MORE = '<!-- more -->'


class Blog(models.Model):

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    entries_per_page = models.IntegerField(default=10)
    recent_entries = models.IntegerField(default=5)
    recent_comments = models.IntegerField(default=5)

    def __unicode__(self):
        return 'Blog(title=%s, subtitle=%s)' % (self.title, self.subtitle)


class Category(models.Model):

    name = models.CharField(max_length=50, db_index=True, unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Tag(models.Model):

    name = models.CharField(max_length=50, db_index=True, unique=True)

    def __unicode__(self):
        return self.name


class EntryStatus(object):
    DRAFT = 'd'
    PUBLISHED = 'p'
    CHOICES = (
        (DRAFT, 'draft'),
        (PUBLISHED, 'published')
    )


class Entry(models.Model):

    title = models.CharField(max_length=100, db_index=True, unique=True)
    slug = models.SlugField(max_length=100)

    created_time = models.DateTimeField(auto_now_add=True)
    published_time = models.DateTimeField(null=True)
    updated_time = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=1, choices=EntryStatus.CHOICES, default=EntryStatus.DRAFT)

    is_public = models.BooleanField(default=True)
    is_top = models.BooleanField(default=False)

    access_count = models.IntegerField(default=1, editable=False)

    category = models.ForeignKey(Category, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, blank=True)

    digest = models.TextField(default='', blank=True)
    content = models.TextField(default='')

    def __unicode__(self):
        return 'Entry(id=%d, title=%s)' % (self.id, self.title)

    def save(self, *args, **kwds):
        if self.digest == '':
            find = self.content.find(MORE)
            if find == -1:
                find = MAX_DIGEST_LEN
            self.digest = self.content[:find]
            if len(self.content) > MAX_DIGEST_LEN:
                self.digest += '...'
        super(Entry, self).save(*args, **kwds)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id, 'slug': self.slug})

    def get_date(self):
        return self.published_time

    def get_author(self):
        return '%s' % self.author
