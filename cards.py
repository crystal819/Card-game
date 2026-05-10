import random
import time
import os

def win_check(player):
    win = True
    suit = player.cards[0].suit
    for i in range(1, len(player.cards)):
        if player.cards[i].suit != suit:
            win = False
            break
    return win

def reward_check(player):
    reward = True
    value = player.cards[0].value
    for i in range(1, len(player.cards)):
        if player.cards[i].value != value:
            reward = False
            break
    return reward


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.string = str(value)+str(suit)

class Player:
    def __init__(self, name, number_of_cards, deck):
        self.name = name
        self.cards = []
        self.bank = []

        for i in range(number_of_cards):
            card = random.randint(0, len(deck)-1)
            self.cards.append(deck[card])
            deck.pop(card)
    
    def get_cards(self):
        return self.cards
    
    def add_bank(self, card):
        self.bank.append(card)

    def get_bank(self):
        return self.bank

    def switch_with_bank(self, card, bank_slot_start=0): #will always return the 0th card from the bank 
        temp = self.bank[bank_slot_start]
        self.bank[bank_slot_start] = card
        return temp
            
    def switch_within_bank(self, bank_slot_start): #will switch the slot and the one after
        temp = self.bank[bank_slot_start]
        self.bank[bank_slot_start] = self.bank[bank_slot_start+1]
        self.bank[bank_slot_start+1] = temp

    def switch_externally(self, own_card_str, new_card, opponent=None):
        for i in range(len(self.cards)):
            if self.cards[i].string == own_card_str:
                if type(opponent) == Player:
                    for j in range(len(opponent.cards)):
                        if opponent.cards[j] == new_card:
                            opponent.cards[j] = self.cards[i]
                            self.cards[i] = new_card
                            return True
                elif type(opponent) == list:
                    for j in range((len(opponent))):
                        if opponent[j] == new_card:
                            opponent[j] = self.cards[i]
                            self.cards[i] = new_card
                            return True
                return False
            
class Game:
    def __init__(self, p1_name, p2_name, level):
        self.values = ['6', '7', '8', '9', '2', '3', '4', '5', 'T', 'J', 'Q', 'K', 'A']
        self.suits = ['d', 'h', 's', 'c']
        self.deck = []



        self.p1 = Player(p1_name, level, self.deck)
        self.p2 = Player(p2_name, level, self.deck)

        while win_check(self.p1) == True or win_check(self.p2) == True:
            self.deck = []
            for i in range(level):
                for j in range(len(self.suits)):
                    self.deck.append(Card(self.values[i], self.suits[j]))
            self.p1 = Player(p1_name, level, self.deck)
            self.p2 = Player(p2_name, level, self.deck)

        self.turn = 'p1'

    def make_move(self, action, card_str, CLI=False):
        if self.turn == 'p1':
            player = self.p1
            opponent = self.p2
        else:
            player = self.p2
            opponent = self.p1

        if card_str in (card.string for card in player.cards):
            if action == opponent:
                return player.switch_externally(card_str, opponent.cards[random.randint(0, len(opponent.cards)-1)], opponent)
            elif action == 'deck':
                return player.switch_externally(card_str, self.deck[random.randint(0, len(self.deck)-1)], self.deck)
        else:
            return False
        
        if win_check(self.p1) == True:
            if CLI == True:
                print(f'{self.p1.name} wins!')
            return self.p1
        elif win_check(self.p2) == True:
            if CLI == True:
                print(f'{self.p2.name} wins!')
            return self.p2
        
        if self.turn == 'p1':
            self.turn = 'p2'
        else:
            self.turn = 'p1'
        return True