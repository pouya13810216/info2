from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Articel

class LiveindexSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Articel.objects.all()

    def lastmod(self, obj):
        return obj.created_at  # یا obj.created_at اگه فیلدی به این نام داشته باشی


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["index", "articels"]  # فقط ویوهایی که پارامتر نمی‌گیرن

    def location(self, item):
        return reverse(item)
