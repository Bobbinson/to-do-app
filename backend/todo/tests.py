from django.test import TestCase
from .models import todo
from django.urls import reverse
#from tastypie.test import ResourceTestCase
# Create your tests here.




class generalTest(TestCase):

    # Testing models.py
    def create_test(self, title="Test", description="This is a test", completed=False):
        return todo.objects.create(title=title, description=description, completed=completed)
    
    def test_test(self):
        w = self.create_test()
        self.assertTrue(isinstance(w,todo))
        self.assertEqual(w.__str__(),w.title)

    # Testing views.py
    # def test_views(self):
    #     w = self.create_test()
    #     url = reverse("/admin")
    #     resp = self.client.get()

    #     self.assertEqual(resp.status_code, 200)
    #     self.assertIn(w.title, resp.content)

# Testing the API

# class entryResourceTest(ResourceTestCase):

#     def test_get_api_json(self):
#         resp = self.api_client.get('/api',format='json')
#         self.assertValidJSONResponse(resp)

#     def test_get_api_xml(self):
#         resp = self.api_client.get('/api', format='xml')
#         self.assertValidXMLResponse(resp)