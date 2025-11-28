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

        #make card list
            card = [suit, rank, value]
            deck.append(card)

    return deck


def main():
    money = db.load_money()
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()


    deck = create_deck()
    random.shuffle(deck)

    player_hand = []
    dealer_hand = []

    for i in range(2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())

    print("test")
    print(f"Money: {money}")
    print(f"Player {player_hand}")
    print(f"Dealer {dealer_hand}")
    print(f"Cards Left {len(deck)}")



if __name__ == '__main__':
    main()
