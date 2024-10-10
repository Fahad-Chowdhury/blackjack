from os import system, name
import random
from art import blackjack_art


def clear():
    ''' Method clear the CLI terminal. '''
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def draw_a_card():
    ''' It picks a random card from the deck. '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
    return random.choice(cards)


def get_user_choice():
    ''' Get input whether user wants to draw another card.
    Keep asking user for input if it is either 'y' / 'n'. '''
    choice = input("\nType 'y' to get another card, type 'n' to pass: ").lower()
    while choice not in ['y', 'n']:
        print("Please only choose y/n. Try again!")
        choice = input("\nType 'y' to get another card, type 'n' to pass: ").lower()
    return choice


def get_remaining_computer_cards(computer_cards):
    ''' It picks the hands for the computer. '''
    while sum(computer_cards) < 17:
        computer_cards.append(draw_a_card())
        if sum(computer_cards) > 21 and 11 in computer_cards:
                computer_cards.remove(11)
                computer_cards.append(1)
    return computer_cards


def select_winner(user_cards, computer_cards):
    ''' Selects and displays a winner based on the drawn cards. '''
    user_total = sum(user_cards)
    comp_total = sum(computer_cards)
    print(f"\n    Your final hand: {user_cards}, score: {user_total}")
    print(f"    Computer's final hand: {computer_cards}, score: {comp_total}")
    if user_total > 21:
        print("\n> You went over, YOU LOSE (ᵟຶ︵ ᵟຶ) \n")
    elif comp_total > 21:
        print("\n> Computer went over, YOU WIN! \\(ᵔᵕᵔ)/ \n")
    elif comp_total > user_total:
        print("\n> Computer has a higher score, YOU LOSE (ᵟຶ︵ ᵟຶ) \n")
    elif comp_total == user_total:
        print("\n> It's a draw! You have the same score as computer! \n")
    else:
        print("\n> Congratulations! You have a higher score, YOU WIN! \\(ᵔᵕᵔ)/ \n")


def blackjack():
    ''' Main functionality of blackjack game. '''
    clear()
    print(blackjack_art)
    user_cards = [draw_a_card() for _ in range(2)]
    computer_cards = []
    computer_cards.append(draw_a_card())
    choice = 'y'
    while choice == 'y' and sum(user_cards) < 21:
        print(f"    Your hand: {user_cards}, score: {sum(user_cards)}")
        print(f"    Computer's hand: {computer_cards}, score: {sum(computer_cards)}")
        choice = input("\nType 'y' to get another card, type 'n' to pass: ")
        if choice == 'y':
            new_card = draw_a_card()
            print(f"    Your drew: {new_card}")
            user_cards.append(new_card)
            if sum(user_cards) > 21 and 11 in user_cards:
                user_cards.remove(11)
                user_cards.append(1)
    if sum(user_cards) <= 21:
        computer_cards = get_remaining_computer_cards(computer_cards)
    select_winner(user_cards, computer_cards)


def main():
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    while choice == 'y':
        blackjack()
        choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


if __name__ == "__main__":
    main()
