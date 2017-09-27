from django.conf.urls import url
from views import MakeView

urlpatterns = [
    url(r'^', MakeView.as_view(), name='card-index'),
]