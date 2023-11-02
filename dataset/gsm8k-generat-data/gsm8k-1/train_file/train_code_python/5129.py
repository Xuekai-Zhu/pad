def solution():
    """Paul has five dogs. For every 10 pounds they weigh, they need 1 pound of dog food per day.
    One weighs 20 pounds. One weighs 40. Another weighs 10. One weighs 30 and the final one weighs 50 pounds.
    How much dog food does he need each day?"""
    total_weight = 20 + 40 + 10 + 30 + 50  # Total weight of all dogs in pounds
    food_per_day = total_weight // 10  # Amount of food needed in pounds per day (rounded down)
    result = food_per_day
    return result

print(solution())