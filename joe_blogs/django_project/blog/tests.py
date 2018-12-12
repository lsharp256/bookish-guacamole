from django.test import TestCase
from django.urls import reverse


class SimpleTest(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_about_page_contains_correct_html(self):
        response = self.client.get('/about/')
        self.assertContains(response, '<h1>About Page</h1>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')
