"""
This script implements a real-time stock trading engine that matches buy and sell orders.
It uses a custom queue implementation to store and process orders sequentially.
"""

import random
import time


# Custom Node class for the queue
class Node:
    """Represents an order in the order book."""
    def __init__(self, order_type, ticker, quantity, price):
        self.order_type = order_type  # 'Buy' or 'Sell'
        self.ticker = ticker  # Stock ticker symbol
        self.quantity = quantity  # Number of shares
        self.price = price  # Price per share
        self.next = None  # Pointer to the next node in the queue


# Custom Queue implementation
class OrderQueue:
    """Queue data structure to store buy and sell orders."""
    def __init__(self):
        self.head = None  # First order in the queue
        self.tail = None  # Last order in the queue

    def enqueue(self, order_type, ticker, quantity, price):
        """Adds a new order to the queue."""
        new_node = Node(order_type, ticker, quantity, price)
        print(f"Inserting new order: {order_type} {quantity} shares of {ticker} at ${price}")
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node

    def dequeue(self):
        """Removes and returns the first order in the queue."""
        if not self.head:
            return None
        removed_node = self.head
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return removed_node

    def is_empty(self):
        """Checks if the queue is empty."""
        return self.head is None


# Create separate queues for Buy and Sell orders
buy_orders = OrderQueue()
sell_orders = OrderQueue()


# Function to add an order to the appropriate queue
def addOrder(order_type, ticker, quantity, price):
    """Adds an order to the buy or sell queue based on order type."""
    if order_type == 'Buy':
        buy_orders.enqueue(order_type, ticker, quantity, price)
    else:
        sell_orders.enqueue(order_type, ticker, quantity, price)


# Function to match buy and sell orders
def matchOrder():
    """Matches buy and sell orders based on price and quantity criteria."""
    while not buy_orders.is_empty() and not sell_orders.is_empty():
        buy_order = buy_orders.dequeue()
        sell_order = sell_orders.dequeue()

        if buy_order.price >= sell_order.price:
            matched_quantity = min(buy_order.quantity, sell_order.quantity)
            print(f"Matched {matched_quantity} shares of {buy_order.ticker} at ${sell_order.price}")

            # If there's remaining quantity, reinsert the leftover order
            if buy_order.quantity > matched_quantity:
                buy_orders.enqueue('Buy', buy_order.ticker, buy_order.quantity - matched_quantity, buy_order.price)
            if sell_order.quantity > matched_quantity:
                sell_orders.enqueue('Sell', sell_order.ticker, sell_order.quantity - matched_quantity, sell_order.price)
        else:
            # Reinsert the orders if they can't be matched
            buy_orders.enqueue(buy_order.order_type, buy_order.ticker, buy_order.quantity, buy_order.price)
            sell_orders.enqueue(sell_order.order_type, sell_order.ticker, sell_order.quantity, sell_order.price)
            break  # Stop processing if no match is found


# Simulate random stock transactions
def simulate_trading():
    """Generates random buy and sell orders and processes them in real-time."""
    tickers = [f"TICKER{i}" for i in range(1, 1025)]  # 1,024 tickers
    # Run a finite number of iterations for controlled execution
    for _ in range(100):
        order_type = random.choice(['Buy', 'Sell'])
        ticker = random.choice(tickers)
        quantity = random.randint(1, 100)
        price = round(random.uniform(10, 500), 2)
        addOrder(order_type, ticker, quantity, price)
        matchOrder()
        # Short sleep time to simulate real-time delays
        time.sleep(random.uniform(0.1, 0.5))


# Running the trading simulation
if __name__ == "__main__":
    simulate_trading()
