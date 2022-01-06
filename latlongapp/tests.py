from django.test import TestCase
from django.urls import reverse

class TestLocalView(TestCase):
    
    def test_local_list_view(self):
        response = self.client.get(reverse('local_list'))
        self.assertEqual(response.status_code, 200)

    def test_local_create_view(self): 
        response = self.client.post(reverse('add_local'), {
            'name':'Nagumo',
            'city': 'São Paulo',
            'latitude': '-23.5817',
            'longitude': '-46.4623',
            'area': '3.9586677',
            'Region': 'Zona Leste',
            'visited': '2020-08-01',            
            
        })        
        
     
    def test_local_update_view(self): 
        response = self.client.put(reverse('local_update', args='1'), {
            'name':'Nagumo',
            'city': 'São Paulo',
            'latitude': '-23.5817',
            'longitude': '-46.4623',
            'area': '3.9586677',
            'Region': 'Zona Leste',
            'visited': '2020-08-01',            
            
        })


    def test_book_delete_view(self): 
        response = self.client.delete(
            reverse('local_delete', args='1'))
