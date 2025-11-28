def load_money():
    try:
        with open("money.txt", "r") as f:
            return float(f.read().strip())
    except FileNotFoundError:
        print("No money file found.")
        print("Starting with 100.0")
        return 100.0