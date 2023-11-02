def solution():
    """Lily goes to the supermarket. She has $60. She needs to buy 6 items: celery, cereal, bread, milk, potatoes, and coffee. She finds a stalk of celery for $5, cereal for 50% off $12, bread for $8, and milk for 10% off $10. She finds potatoes for $1 each and buys 6. How many dollars does she have left to spend on coffee?"""
    total_budget = 60
    celery_price = 5
    cereal_price = 12 * 0.5
    bread_price = 8
    milk_price = 10 * 0.9
    potatoes_price = 1 * 6
    total_spent = celery_price + cereal_price + bread_price + milk_price + potatoes_price
    remaining_budget = total_budget - total_spent
    result = remaining_budget
    return result

print(solution())