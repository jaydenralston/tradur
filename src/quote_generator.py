def generate_quotes(current_price, spread = 0.1, inventory = 0, inventory_skew = 0.01):
    """
    Generates bid and ask prices around a fair price.

    current_price: the current price
    spread: the gap between the bid and ask prices
    inventory_skew: how strongly the amount of inventory the bot has affects the current/quote price

    bid: buy
    ask: sell
    """

    # If inventory is positive, lower quotes to encourage selling. <- this is an easy way to remember
    # If inventory is negative, raise quotes to encourage buying.

    skew_adjustment = inventory * inventory_skew

    adjusted_price = current_price - skew_adjustment # e.g. if inventory is 10 the adjusted price will be lower than current so traders are more likely to buy from the bot so the bot can sell

    bid_price = adjusted_price - spread / 2 # buy here. e.g. current_price = 100, bid_price = 100 - 0.1/2 = 100 - 0.05 = 99.95
    ask_price = adjusted_price + spread / 2 # sell here. e.g. current_price = 100, ask_price = 100 + 0.1/2 = 100 + 0.05 = 100.05

    return bid_price, ask_price
