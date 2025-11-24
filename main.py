def load_money():
    try:
        with open("money.txt","r") as f:
            return float(f.read().strip())
    except FileNotFoundError:
        print("No money file found.")


def create_deck():
    #sorted by suits

    suits = ["Diamonds", "Clubs", "Spades", "Hearts"]
    
    ace_of_diamonds = 11 #or 1
    ace_of_hearts = 11  # or 1
    ace_of_spades = 11  # or 1
    ace_of_clubs = 11  # or 1

    queen_of_diamonds = 10
    queen_of_hearts = 10
    queen_of_spades = 10
    queen_of_clubs = 10

    king_of_diamonds = 10
    king_of_hearts = 10
    king_of_spades = 10
    king_of_clubs = 10

    jack_of_diamonds = 10
    jack_of_hearts = 10
    jack_of_spades = 10
    jack_of_clubs = 10

    ten_of_diamonds = 10
    ten_of_hearts = 10
    ten_of_spades = 10
    ten_of_clubs = 10

    nine_of_diamonds = 9
    nine_of_hearts = 9
    nine_of_spades = 9
    nine_of_clubs = 9

    eight_of_diamonds = 8
    eight_of_hearts = 8
    eight_of_spades = 8
    eight_of_clubs = 8

    seven_of_diamonds = 7
    seven_of_hearts = 7
    seven_of_spades = 7
    seven_of_clubs = 7

    six_of_diamonds = 6
    six_of_hearts = 6
    six_of_spades = 6
    six_of_clubs = 6

    five_of_diamonds = 5
    five_of_hearts = 5
    five_of_spades = 5
    five_of_clubs = 5

    four_of_diamonds = 4
    four_of_hearts = 4
    four_of_spades = 4
    four_of_clubs = 4

    three_of_diamonds = 3
    three_of_hearts = 3
    three_of_spades = 3
    three_of_clubs = 3

    two_of_diamonds = 2
    two_of_hearts = 2
    two_of_spades = 2
    two_of_clubs = 2

    one_of_diamonds = 1
    one_of_hearts = 1
    one_of_spades = 1
    one_of_clubs = 1





def main():
    load_money()
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

    



if __name__ == '__main__':
    main()