def generate_quotes(current_price, spread = 0.1):
    """
    Generates bid and ask prices around a fair price.

    current_price: the current price
    spread: the gap between the bid and ask prices

    bid: buy
    ask: sell
    """

    bid_price = current_price - spread / 2 # buy here. e.g. current_price = 100, bid_price = 100 - 0.1/2 = 100 - 0.05 = 99.95
    ask_price = current_price + spread / 2 # sell here. e.g. current_price = 100, bid_price = 100 + 0.1/2 = 100 + 0.05 = 100.05

    return bid_price, ask_price
