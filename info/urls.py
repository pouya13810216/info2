from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from hom.sitemaps import StaticViewSitemap, LiveindexSitemap

sitemaps = {
    "articles": LiveindexSitemap,
    "static": StaticViewSitemap,
}

urlpatterns = [
    path('admins/', admin.site.urls),
    path('', include('hom.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]
