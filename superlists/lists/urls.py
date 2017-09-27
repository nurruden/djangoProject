from django.conf.urls import url,include

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]
from .views import home_page

urlpatterns = []
urlpatterns+=[url(r'^$', home_page)]
