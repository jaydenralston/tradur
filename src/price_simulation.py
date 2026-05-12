import numpy as np

def simulate_price(start_price = 100, steps = 500, volatility = 0.2):
    """
    Simulates a fake price chart that goes randomly up and down over time.

    start_price: The price the chart starts at.

    steps: How many times the price changes.

    volatility: Controls how jumpy the price is. 0.2 means it'll jump up and down ~0.2 or 20 cents in this case since start price is $100
    A higher number means bigger random movements.
    """

    prices = [start_price]

    for _ in range(steps):
        price_change = np.random.normal(0, volatility)
        new_price = prices[-1] + price_change # old price + price_change which is randomly generated like 0.2, -0.13, 0.3 etc with np.random.normal(0, 0.2)

        if new_price <= 0:
            new_price = 0.01

        prices.append(new_price) # adds every updated price to list

    return prices