from django.urls import reverse, resolve
from django.test import TestCase
from todo_list.views import todo_view, about_view, update, deleteTodo



class TestUrls(TestCase):

    def test_home_url(self):
        url = reverse('Home')
        self.assertEquals(resolve(url).func, todo_view)

    def test_update_url(self):
        url = reverse('update')
        self.assertEquals(resolve(url).func, update)

    

    