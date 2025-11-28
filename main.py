import db

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
    db.load_money()
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")


if __name__ == '__main__':
    main()
