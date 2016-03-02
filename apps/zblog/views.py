from collections import defaultdict

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response
from django.shortcuts import get_list_or_404

from .models import *


def admin_criteria(request):
    criteria = {'status': EntryStatus.PUBLISHED}
    if not (request.user and request.user.is_superuser):
        criteria['is_public'] = True
    return criteria


def index(request):
    return page(request, page_num='1')


def page(request, page_num=None):
    blog = Blog.objects.get()
    paginator = Paginator(get_list_or_404(
        Entry.objects.order_by('-published_time'),
        **admin_criteria(request)
    ), blog.entries_per_page)

    try:
        entries = paginator.page(page_num)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)

    return render_to_response('blog/page.html', locals())


def detail(request, id=None, slug=None):
    blog = Blog.objects.get()
    entry = Entry.objects.get(id=id)
    entry.access_count += 1
    return render_to_response('blog/detail.html', locals())


def archives(request):
    blog = Blog.objects.get()
    entries = Entry.objects.order_by('published_time').all()
    d = defaultdict(list)
    for e in entries:
        year = e.published_time.year
        month = e.published_time.month
        d[(year, month)].append(e)
    archives_items = d.items()
    return render_to_response('blog/archives.html', locals())


def category(request, category_name=None):
    blog = Blog.objects.get()
    entries = get_list_or_404(
        Entry.objects.order_by('-published_time'),
        category__in=Category.objects.filter(name=category_name),
        **admin_criteria(request)
    )
    return render_to_response('blog/category.html', locals())


def tag(request, tag_name=None):
    blog = Blog.objects.get()
    entries = get_list_or_404(
        Entry.objects.order_by('-published_time'),
        tags__in=Tag.objects.filter(name=tag_name),
        **admin_criteria(request)
    )
    return render_to_response('blog/tag.html', locals())
