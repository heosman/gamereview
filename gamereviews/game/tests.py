from django.test import TestCase
from django.contrib.auth.models import User
from .models import Game
import datetime
from django.urls import reverse_lazy, reverse

# Create your tests here.
class GameTest(TestCase):
   def setUp(self):
       self.type=Game(gamename='Limbo')
       self.user=User(username='user1')
       self.game=Game(gamename='Limbo', genre='Adventure, Puzzle', rating='5 stars', description="n/a", user=self.user, dateentered=5/28/21)

   def test_string(self):
       self.assertEqual(str(self.game), 'Limbo')

   def test_tablename(self):
       self.assertEqual(str(Game._meta.db_table), 'game')
