import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from Task1.models import Game

# Ваш код для работы с моделью Game
games = Game.objects.all()
for game in games:
    print(f"Title: {game.title}, Description: {game.description}, Cost: {game.cost}")
