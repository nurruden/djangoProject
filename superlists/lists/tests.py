from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/lists/')
        self.assertEqual(found.func,home_page)
    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expectd_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(),expectd_html)