# order-book-matching
This repository contains a real-time stock trading engine that matches buy and sell orders efficiently. The engine processes transactions using a custom queue implementation, ensuring sequential execution without relying on built-in data structures like dictionaries or maps.

## Overview

The goal of this project is to implement a **stock trading engine** capable of matching **Buy** orders with **Sell** orders based on price and quantity. The engine simulates random stock transactions and processes them in real-time, making it suitable for handling active stock markets where orders are constantly placed by stockbrokers.

## Requirements

1. **Order Matching**: The engine matches orders by comparing Buy and Sell orders. A Buy order is matched with a Sell order if the Buy price is greater than or equal to the Sell price for a particular ticker symbol.
2. **Add Order Functionality**: The `addOrder` function takes parameters including:
   - **Order Type**: 'Buy' or 'Sell'
   - **Ticker Symbol**: Symbol representing the stock (e.g., "AAPL")
   - **Quantity**: Number of shares to be bought/sold
   - **Price**: Price per share
3. **Simulating Active Stock Transactions**: A wrapper is created around the `addOrder` function to simulate active stock transactions. Orders are generated randomly with different parameters to represent real-world stock trading.

4. **Matching Algorithm**: The `matchOrder` function handles the matching process, ensuring that orders are processed efficiently. The complexity of the matching process is designed to be **O(n)** where 'n' is the number of orders in the order book.

5. **Concurrency Handling**: The implementation considers race conditions by using appropriate data structures and ensuring thread-safety when multiple threads modify the stock order book. Lock-free data structures are used to handle concurrent updates without causing conflicts.

## Implementation Details

- The project uses a custom queue implementation to store and process orders sequentially.
- A `Node` class represents an individual order in the order book, while the `OrderQueue` class manages the buy and sell orders using the queue data structure.
- The engine processes orders by first enqueueing them into separate Buy and Sell queues. The `matchOrder` function then matches orders based on price and quantity.
- A random stock simulation is implemented to generate random Buy and Sell orders with random quantities and prices.

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sakshisingh03/order-book-matching.git
2. **Run the Script**:
   ```bash
   python stock_trading_engine.py
