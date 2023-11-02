def solution():
    """Paul has five dogs. For every 10 pounds they weigh, they need 1 pound of dog food per day. One weighs 20 pounds. One weighs 40. Another weighs 10. One weighs 30 and the final one weighs 50 pounds. How much dog food does he need each day?"""
    dog_weights = [20, 40, 10, 30, 50]
    total_weight = sum(dog_weights)
    food_per_day = total_weight / 10
    result = food_per_day
    return result

print(solution())