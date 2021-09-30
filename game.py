import random


suits = ('Червы', 'Бубны', 'Пики', 'Трефы')
ranks = ('Двойка', 'Тройка', 'Четвёрка', 'Пятерка', 'Шестёрка',
         'Семёрка', 'Восьмёрка', 'Девятка', 'Десятка', 'Валет', 'Дама', 'Король', 'Туз')
values = {'Двойка': 2, 'Тройка': 3, 'Четвёрка': 4, 'Пятерка': 5, 'Шестёрка':  6, 'Семёрка': 7,
          'Восьмёрка': 8, 'Девятка': 9, 'Десятка': 10, 'Валет': 10, 'Дама': 10, 'Король': 10, 'Туз': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'В колоде находятся:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


test_deck = Deck()
print(test_deck)
