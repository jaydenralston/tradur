import numpy as np

def generate_order_event(buy_probability = 0.3, sell_probability = 0.3):
    """
    Randomly decides what will happen at one of the 500 price updates. This could be a 'buy', 'sell' or 'none' nothing happens.

    30% chance a trader buys from the bot
    30% chance a trader sells to the bot
    40% chance nothing happens
    """

    random_number = np.random.random() # creates a random number between 0 and 1, e.g. 0.48

    if random_number < buy_probability: 
        return "buy"
    
    if random_number < buy_probability + sell_probability: # will only return if below 60 but if below 30 it'll return to previous if statement
        return "sell"

    return "none"
