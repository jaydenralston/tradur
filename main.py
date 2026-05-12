import matplotlib.pyplot as plt
from src.price_simulation import simulate_price # imports the function inside this source file so it can be used in this file
from src.quote_generator import generate_quotes
from src.market_bot import MarketBot # imports the class inside this source file with functions inside it
from src.order_flow import generate_order_event


def main():
    prices = simulate_price(start_price = 100, steps = 500, volatility = 0.2) # e.g 101.23, 99.67 etc

    bot = MarketBot(starting_cash = 10000)

    bid_prices = [] # empty arrays
    ask_prices = [] 
    inventory_history = []
    pnl_history = []

    for current_price in prices:
        bid_price, ask_price = generate_quotes(current_price, spread = 0.1, inventory = bot.inventory, inventory_skew = 0.01)

        event = generate_order_event(buy_probability = 0.3, sell_probability = 0.3)

        if event == "buy":
            # Trader buys from the bot, so bot sells at ask price
            bot.sell(ask_price) # look at line 11 if confused why its bot.sell then look into market_bot module
        elif event == "sell":
            # Trader sells to the bot, so bot buys at bid price
            bot.buy(bid_price)

        pnl = bot.calculate_pnl(current_price)

        bid_prices.append(bid_price) # appends bid_price at the current_price onto the list
        ask_prices.append(ask_price)
        inventory_history.append(bot.inventory)
        pnl_history.append(pnl)

    plt.plot(prices, label = "Current Price")
    plt.plot(bid_prices, label = "Bid Price")
    plt.plot(ask_prices, label = "Ask Price")
    plt.title("Tradur: Bid and Ask Quote Generation")
    plt.xlabel("Price Update") # Index numbers of list/how many times price changes.
    plt.ylabel("Price") # Actual Values in the list
    plt.legend()
    plt.show()

    plt.plot(inventory_history)
    plt.title("Tradur: Bot Inventory")
    plt.xlabel("Price Update")
    plt.ylabel("Inventory")
    plt.show()

    plt.plot(pnl_history)
    plt.title("Tradur: Bot PnL")
    plt.xlabel("Price Update")
    plt.ylabel("PnL")
    plt.show()

if __name__ == "__main__": # Start program basically
    main()