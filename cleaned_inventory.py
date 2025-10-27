"""
Inventory Management System
Provides functions to add, remove, load, save, and check stock items.
"""

import json

# Global variable to hold inventory data
stock_data = {}


def add_item(item_name, quantity=0):
    """Add a new item or increase quantity of an existing one."""
    if item_name in stock_data:
        stock_data[item_name] += quantity
    else:
        stock_data[item_name] = quantity
    print(f"Added/Updated {item_name}: {quantity}")


def remove_item(item_name):
    """Remove an item from stock if it exists."""
    try:
        del stock_data[item_name]
        print(f"Removed item: {item_name}")
    except KeyError:
        print(f"Item '{item_name}' not found. Nothing removed.")


def get_quantity(item_name):
    """Return quantity for a given item."""
    return stock_data.get(item_name, 0)


def load_data(filename):
    """Load inventory data from a JSON file."""
    global stock_data
    try:
        with open(filename, "r", encoding="utf-8") as file:
            stock_data = json.load(file)
            print("Data loaded successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with empty stock.")
        stock_data = {}


def save_data(filename):
    """Save inventory data to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(stock_data, file, indent=4)
    print("Data saved successfully.")


def print_data():
    """Print all inventory items."""
    print("Current Inventory:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """List items with stock below a certain threshold."""
    low_items = [item for item, qty in stock_data.items() if qty < threshold]
    print(f"Low stock items (below {threshold}): {low_items}")
    return low_items


if __name__ == "__main__":
    load_data("stock.json")
    add_item("apple", 10)
    add_item("banana", 3)
    remove_item("orange")
    print_data()
    check_low_items()
    save_data("stock.json")
