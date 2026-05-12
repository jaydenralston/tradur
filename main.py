import matplotlib.pyplot as plt
from src.price_simulation import simulate_price # imports the function inside this source file so it can be used in this file


def main():
    prices = simulate_price(start_price = 100.0, steps = 500, volatility = 0.2) # e.g 101.23, 99.67 etc

    plt.plot(prices)
    plt.title("Tradur: Simulated Asset Price")
    plt.xlabel("Price Update") # Index numbers of list/how many times price changes.
    plt.ylabel("Price") # Actual Values in the list
    plt.show()


if __name__ == "__main__": # Start program basically
    main()