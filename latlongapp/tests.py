from django.test import TestCase, Client
from django.urls import reverse
from .models import Local
from django.contrib.auth.models import User

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


    def test_local_delete_view(self): 
        response = self.client.delete(
            reverse('local_delete', args='1'))

class TestLocalModel(TestCase):
    """Test the local model."""
    def setUp(self):
        self.l = Local(name='davo',address='avenida marechal tito', city='são paulo', lat= '-23.5817', lon= '-46.4623', area ='1000000',
                       
                       region='leste', visited='2021-08-01')

    def test_create_local(self):
        self.assertIsInstance(self.l, Local)

    def test_str_representation(self):
        self.assertEquals(str(self.l), "davo")


class TestLoggedInLocalView(TestCase):
    """Test the greeting view for the authenticated users."""
    def setUp(self):
        test_user = User.objects.create_user(username='ani', password='12345')
        test_user.save()
        self.client = Client()



    def test_user_authenticated(self):
        login = self.client.login(username='ani', password='12345')
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)        


        

