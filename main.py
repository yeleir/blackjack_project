def load_money():
    try:
        with open("money.txt","r") as f:
            return float(f.read().strip())
    except FileNotFoundError:
        print("No money file found.")

def main():
    load_money()
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    



if __name__ == '__main__':
    main()