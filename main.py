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
        if response.lower() == "y":
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
            bet_amount = input("Bet Amount:")
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


def get_score(hand):
    total = 0
    aces = 0
    for card in hand:
        total += card[2]
    return total


def ace_choice(hand):
    score = get_score(hand)
    last_card = hand[-1]

    if last_card[1] == "Ace":
        if score > 21:
            print("You got a ace, but 11 would make you go over 21.\bConverting the 11 to a 1.")
            last_card[2] = 1
        else:
            print(f"hand {hand}")
            while True:
                choice = input("You drew a Ace! Would you like to count it as 11 or 1?\b")
                if choice == "1":
                    last_card[2] = 1
                    break
                elif choice == "11":
                    last_card[2] = 11
                    break
                else:
                    print("Please enter either 1 or 11.")


def dealer_aces(hand):
    score = get_score(hand)
    for card in hand:
        if card[1] == "Ace" and score > 21:
            card[2] = 1
            score = get_score(hand)



def main():
    money = db.load_money()
    money = buy_chips(money)
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()

    # bet = grab_bet(money)

    deck = create_deck()
    random.shuffle(deck)

    player_hand = []
    dealer_hand = []

    for i in range(2):
        player_hand.append(deck.pop())
        ace_choice(player_hand)

        dealer_hand.append(deck.pop())
        dealer_aces(dealer_hand)
    player_score = get_score(player_hand)
    dealer_score = get_score(dealer_hand)

    print("test")
    # print(f"Bet: {bet}")
    print("--------------------------")
    print(f"Money: {money}")
    print("--------------------------")
    print(f"Player {player_hand}")
    print(f"Player Score: {player_score}")
    print("--------------------------")
    print(f"Dealer {dealer_hand}")
    print(f"Dealer Score: {dealer_score}")
    print("--------------------------")
    print(f"Cards Left {len(deck)}")
    print("--------------------------")


if __name__ == '__main__':
    main()
