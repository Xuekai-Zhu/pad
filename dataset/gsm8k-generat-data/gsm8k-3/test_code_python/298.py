def solution():
    """Chelsea has 24 kilos of sugar. She divides them into 4 bags equally. Then one of the bags gets torn and half of the sugar falls to the ground. How many kilos of sugar remain?"""
    # Calculate the amount of sugar in each bag
    sugar_per_bag = 24/4

    # Calculate the amount of sugar lost due to the torn bag
    lost_sugar = sugar_per_bag / 2

    # Calculate the amount of sugar remaining
    remaining_sugar = (sugar_per_bag * 3) - lost_sugar

    # Display the amount of sugar remaining
    result = remaining_sugar
    return result

print(solution())