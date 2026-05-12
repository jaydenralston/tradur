class MarketBot: # a class is a blueprint/template used to create objects. think of it as a recipe
    """
    A simple market trading bot that acts as a market maker. It tracks cash, inventory and PnL.
    """

    def __init__(self, starting_cash = 10000):
        self.starting_cash = starting_cash
        self.cash = starting_cash
        self.inventory = 0

    def buy(self, price, quantity = 1):
        """
        Bot buys at a bid price, its cash goes down depending on the price and how much it bought and inventory goes up
        """
        self.cash -= price * quantity
        self.inventory += quantity

    def sell(self, price, quantity = 1):
        """
        Bot sells at an ask price, its cash goes up depending on the price and how much it sold and inventory goes down
        """
        self.cash += price * quantity
        self.inventory -= quantity

    def calculate_pnl(self, current_price):
        """
        Calculates PnL that is compared to the cash that was started with.

        Total Value = cash + value of the inventory
        PnL = total value - starting cash
        """
        total_value = self.cash + self.inventory * current_price
        pnl = total_value - self.starting_cash

        return pnl

