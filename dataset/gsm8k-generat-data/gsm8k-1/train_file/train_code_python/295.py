def solution():
    """Chelsea has 24 kilos of sugar. She divides them into 4 bags equally. Then one of the bags gets torn and half of the sugar falls to the ground. How many kilos of sugar remain?"""
    initial_sugar = 24
    bags = 4
    sugar_per_bag = initial_sugar / bags
    torn_bag_sugar = sugar_per_bag / 2
    remaining_sugar = (bags - 1) * sugar_per_bag - torn_bag_sugar
    result = remaining_sugar
    return result

print(solution())