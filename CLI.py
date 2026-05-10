from cards import Game

def game_function():
    level = int(input("Enter what level you want to play (2, 3 or 4 different value cards): "))
    p1 = input('Enter player 1s name: ')
    p2 = input("Enter player 2s name: ")

    game = Game(p1, p2, level)

    print(f"Cards: {', '.join(card.string for card in p1.cards)}")
    action = input(f"{p1.name}, do you want to trade with {p2.name} or with the deck? ")
    card_str = input("which card do you want to trade? " + ', '.join(card.string for card in p2.cards) + ' : ')

    temp = game.make_move(action, card_str, CLI=True)
    while temp == False:
        if game.turn == 'p1':
            print(f"Cards: {', '.join(card.string for card in p1.cards)}")
            action = input(f"{p1.name}, do you want to trade with {p2.name} or with the deck? ")
            card_str = input("which card do you want to trade? " + ', '.join(card.string for card in p2.cards) + ' : ')

            temp = game.make_move(action, card_str, CLI=True)
        elif game.turn == 'p2':
            print(f"Cards: {', '.join(card.string for card in p2.cards)}")
            action = input(f"{p2.name}, do you want to trade with {p1.name} or with the deck? ")
            card_str = input("which card do you want to trade? " + ', '.join(card.string for card in p1.cards) + ' : ')

            temp = game.make_move(action, card_str, CLI=True)
    if temp != True:
        play_again = input("Do you want to play again: ")
        if play_again == 'Yes':
            game_function()


if __name__ == '__main__':
    game_function()