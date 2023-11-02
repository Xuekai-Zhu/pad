def solution():
    """For the family reunion, Peter is buying 16 pounds of bone-in chicken and half that amount in hamburgers. He's going to buy 2 more pounds of hot dogs than hamburgers. He's also going to buy several sides that will weigh half the amount of hot dogs. How many pounds of food will he buy?"""
    # Define the weight of bone-in chicken
    chicken_weight = 16

    # Define the weight of hamburgers
    hamburger_weight = chicken_weight / 2

    # Define the weight of hot dogs
    hotdog_weight = hamburger_weight + 2

    # Define the weight of sides
    sides_weight = hotdog_weight / 2

    # Calculate the total weight of food
    total_weight = chicken_weight + hamburger_weight + hotdog_weight + sides_weight

    # Return the result
    result = total_weight
    return result

print(solution())