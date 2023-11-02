def solution():
    """Paul has five dogs. For every 10 pounds they weigh, they need 1 pound of dog food per day. One weighs 20 pounds. One weighs 40. Another weighs 10. One weighs 30 and the final one weighs 50 pounds. How much dog food does he need each day?"""
    # Define the weight of each dog in pounds
    dog1_weight = 20
    dog2_weight = 40
    dog3_weight = 10
    dog4_weight = 30
    dog5_weight = 50

    # Calculate the total weight of all dogs
    total_weight = dog1_weight + dog2_weight + dog3_weight + dog4_weight + dog5_weight

    # Calculate the total amount of dog food needed per day
    food_per_day = total_weight / 10

    result = food_per_day
    return result

print(solution())