from django.contrib.sitemaps import Sitemap
from .models import *

from django.urls import reverse


class CustomerSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1
    protocol = 'https'

    def items(self):
        return Customer.objects.all()

    def lastmod(self, obj):
        return obj.modified

   # def location(self,obj):
    #    return '/blog/%s' % (obj.article_slug)


class ProductSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1
    protocol = 'https'

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.modified

   # def location(self,obj):
    #    return '/blog/%s' % (obj.article_slug)


class IzdavastvoSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    

    def items(self):
        return Izdavastvo.objects.all()

   # def location(self,obj):
    #    return '/blog/%s' % (obj.article_slug)


class KursSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Kurs.objects.all()

    def lastmod(self, obj):
        return obj.modified

  #  def location(self,obj):
   #     return '/blog/%s' % (obj.article_slug)



class OrderSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Order.objects.all()

    def lastmod(self, obj):
        return obj.modified

 #   def location(self,obj):
  #      return '/blog/%s' % (obj.article_slug)


class OrderItemSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return OrderItem.objects.all()

    def lastmod(self, obj):
        return obj.modified

 #   def location(self,obj):
  #      return '/blog/%s' % (obj.article_slug)


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['store'] #ovo ne kontam

    def location(self, item):
        return reverse(item)