import matplotlib.pyplot as plt
from src.price_simulation import simulate_price # imports the function inside this source file so it can be used in this file
from src.quote_generator import generate_quotes


def main():
    prices = simulate_price(start_price = 100, steps = 500, volatility = 0.2) # e.g 101.23, 99.67 etc

    bid_prices = [] # empty arrays
    ask_prices = [] 

    for current_price in prices:
        bid_price, ask_price = generate_quotes(current_price, spread = 0.1)

        bid_prices.append(bid_price) # appends bid_price at the current_price onto the list
        ask_prices.append(ask_price)

    plt.plot(prices, label = "Current Price")
    plt.plot(bid_prices, label = "Bid Price")
    plt.plot(ask_prices, label = "Ask Price")
    plt.title("Tradur: Bid and Ask Quote Generation")
    plt.xlabel("Price Update") # Index numbers of list/how many times price changes.
    plt.ylabel("Price") # Actual Values in the list
    plt.legend()
    plt.show()


if __name__ == "__main__": # Start program basically
    main()