from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from sirmvit import views as core_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$',core_views.front, name='front'),
    url(r'home', core_views.home, name='home'),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^admin/', admin.site.urls),
    # url(r'^percent/', core_views.percent,name='percent'),
        url(r'^search/',core_views.search ,name="search"),
        # url(r'^accounts/', admin.site.urls),
        # url(r'^blog_search_list_view/?$', 'core_views.BlogSearchListView', name='your_url_name'),

    # url(r'^about/',core_views.about, name='about'),
    # url(r'^checkout/',core_views.checkout, name='checkout'),
    # url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^product_list/$', core_views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', core_views.product_list, name='product_list_by_category'),
    # url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',core_views.product_detail,name='product_detail'),

]
admin.site.site_header = settings.ADMIN_SITE_HEADER
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
