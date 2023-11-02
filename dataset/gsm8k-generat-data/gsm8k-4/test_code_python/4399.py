def solution():
    """Lily goes to the supermarket. She has $60. She needs to buy 6 items: celery, cereal, bread, milk, potatoes, and coffee. She finds a stalk of celery for $5, cereal for 50% off $12, bread for $8, and milk for 10% off $10. She finds potatoes for $1 each and buys 6. How many dollars does she have left to spend on coffee?"""
    # Define the amount of money Lily has to spend
    budget = 60

    # Define the prices of each item
    celery_price = 5
    cereal_price = 12 * 0.5
    bread_price = 8
    milk_price = 10 * 0.9
    potato_price = 1
    coffee_price = None

    # Calculate the total cost of the items purchased so far
    total_cost = celery_price + cereal_price + bread_price + milk_price + (potato_price * 6)

    # Calculate the remaining budget
    remaining_budget = budget - total_cost

    # Set the price of coffee to the remaining budget
    coffee_price = remaining_budget

    # Return the price of coffee
    result = coffee_price
    return result

print(solution())