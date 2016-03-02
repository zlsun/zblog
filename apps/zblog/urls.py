from django.conf.urls import patterns, url

urlpatterns = patterns(
    'apps.zblog.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<id>\d+)/(?P<slug>[\w_-]+)', 'detail', name='detail'),
    url(r'^archives', 'archives', name='archives'),
    url(r'^tag/(?P<tag_name>.+)', 'tag', name='tag'),
    url(r'^category/(?P<category_name>.+)', 'category', name='category'),
    url(r'^page/(?P<page_num>\d+)', 'page', name='page'),
)
