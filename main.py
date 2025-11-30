import sys
import db
import random


def create_deck():
    suits = ["Diamonds", "Clubs", "Spades", "Hearts"]
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "King", "Queen", "Jack", "Ace"]
    deck = []
    for suit in suits:
        for rank in ranks:
            if rank in ["Jack", "Queen", "King"]:
                value = 10
            elif rank == "Ace":
                value = 11
            else:
                value = rank
            card = [suit, rank, value]
            deck.append(card)

    return deck


def buy_chips(money):
    current_money = money
    if current_money < 5:
        print(f"You only have {money}. You need at least 5 chips.")
        response = input("Do you want to buy chips? (y/n): ")
        if response.lower == "y":
            money += 100
            db.save_money(money)
            print(f"Added 100. New balance: {money}")
        else:
            print("Thanks for playing!")
            sys.exit()
    return money


def grab_bet(money):
    while True:
        try:
            bet_amount = input("Bet Amount:\n")
            bet = float(bet_amount)
            if bet < 5:
                print(f"Minimum bet is 5. You have {money}.")
            elif bet > 1000:
                print(f"Maximum bet is 1000.")
            elif bet > money:
                print(f"You don't have enough money.\bCurrent money is {money}.")
            else:
                return bet
        except ValueError:
            print("Please enter a numeric value.")


def main():
    money = db.load_money()
    money = buy_chips(money)
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()

    bet = grab_bet(money)

    deck = create_deck()
    random.shuffle(deck)

    player_hand = []
    dealer_hand = []

    for i in range(2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())

    print("test")
    print(f"Bet: {bet}")
    print(f"Money: {money}")
    print(f"Player {player_hand}")
    print(f"Dealer {dealer_hand}")
    print(f"Cards Left {len(deck)}")


if __name__ == '__main__':
    main()
