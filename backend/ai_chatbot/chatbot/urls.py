from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import include, url
from django.conf import settings

from .views import updateUser, chat, getAuthor


urlpatterns = [
    url(r'^updateUser/', updateUser),
    url(r'^chat', chat, name="chatfunctions"),
    url(r'^getauthor/(?P<u_id>\d{1,3})/$', getAuthor),
    # url(r'^image_resize/$',users.image_resize),

    # url(r'^export_users_xls/', leavereport.export_users_xls),





]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)
