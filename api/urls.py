from django.conf.urls import url
from api.views import do_get_pan_data


urlpatterns = [
    url('^get-pan-data/$', do_get_pan_data)
]