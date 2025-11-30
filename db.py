def load_money():
    try:
        with open("money.txt", "r") as f:
            return float(f.read().strip())
    except FileNotFoundError:
        print("No money file found.")
        print("Starting with 100.0")
        return 100.0
    except ValueError:
        print("Money file is empty. Resetting to 100.0")
        return 100.0

def save_money(amount):
    with open("money.txt", "w") as f:
        f.write(str(amount))