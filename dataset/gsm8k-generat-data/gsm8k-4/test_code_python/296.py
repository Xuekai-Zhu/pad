def solution():
    """Chelsea has 24 kilos of sugar. She divides them into 4 bags equally.
    Then one of the bags gets torn and half of the sugar falls to the ground.
    How many kilos of sugar remain?"""
    # Define the initial amount of sugar
    initial_sugar = 24

    # Divide the sugar into 4 equal bags
    equal_bags = initial_sugar / 4

    # One of the bags gets torn and half of the sugar falls to the ground
    remaining_sugar = equal_bags * 3 - (equal_bags / 2)

    # Return the amount of sugar that remains
    result = remaining_sugar
    return result

print(solution())