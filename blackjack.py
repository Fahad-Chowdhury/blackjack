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


def check_for_aces(cards):
    ''' It checks for aces (11) and replaces with one if sum exceeds 21. '''
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return cards


def get_remaining_computer_cards(computer_cards):
    ''' It picks the hands for the computer. '''
    while sum(computer_cards) < 17:
        computer_cards.append(draw_a_card())
        computer_cards = check_for_aces(computer_cards)
    return computer_cards


def print_blackjack_message(user_total, comp_total):
    ''' Print message if it's a blackjack. '''
    if user_total == 21 == comp_total:
        print("\nYou and computer both have a BLACKJACK!")
    elif user_total == 21:
        print("\nYou have a BLACKJACK!")
    elif comp_total == 21:
        print("\nComputer has a BLACKJACK!")


def display_winning_message(user_total, comp_total):
    ''' Print winning message. '''
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


def select_winner(user_cards, computer_cards):
    ''' Selects and displays a winner based on the drawn cards. '''
    user_total = sum(user_cards)
    comp_total = sum(computer_cards)
    print(f"\n    Your final hand: {user_cards}, score: {user_total}")
    print(f"    Computer's final hand: {computer_cards}, score: {comp_total}")
    print_blackjack_message(user_total, comp_total)
    display_winning_message(user_total, comp_total)


def blackjack():
    ''' Main functionality of blackjack game. '''
    clear()
    print(blackjack_art)

    user_cards = [draw_a_card() for _ in range(2)]
    computer_cards = [draw_a_card()]

    # Finalize user cards
    choice = 'y'
    while choice == 'y' and sum(user_cards) < 21:
        print(f"    Your hand: {user_cards}, score: {sum(user_cards)}")
        print(f"    Computer's hand: {computer_cards}, score: {sum(computer_cards)}")
        choice = input("\nType 'y' to get another card, type 'n' to pass: ")
        if choice == 'y':
            new_card = draw_a_card()
            user_cards.append(new_card)
            print(f"    Your drew: {new_card}")
            user_cards = check_for_aces(user_cards)

    # Get all the computer's card if user is not over 21
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
