from random import randint
import requests
import telebot
from config import token


from random import randint

bot = telebot.TeleBot(token)

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.hp = randint(50,100)
        self.power = randint(10,20)
        self.img = self.get_img()
        self.name = self.get_name()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"""Имя твоего покеомона: {self.name}
Здоровье покемона: {self.hp}
Сила покемона: {self.power}
"""

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

    def attack(self,enemy):
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Сражение @{self.pokemon_trainer} над @{enemy.pokemon_trainer}"

class Wizard(Pokemon):
    def info(self):
        return f"Покемон Волшебник: {super().info()}"

class Fighter(Pokemon):
    def attack(self, enemy):
        superpower = randint(5,15)
        self.power += superpower
        result = super().attack(enemy)
        self.power -= superpower
        return result + f"\nБоец применил суператаку с силой в {superpower}"

    def info(self):
        return f"Покемон: {super().info()}"

if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))

@bot.message_handler(commands=['go'])
def start(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")
class Wizard(Pokemon):
    def info(self):
        return f"Покемон Волшебник: {super().info()}"


