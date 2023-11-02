def solution():
    """Chelsea has 24 kilos of sugar. She divides them into 4 bags equally. Then one of the bags gets torn and half of the sugar falls to the ground. How many kilos of sugar remain?"""
    total_sugar = 24
    sugar_per_bag = total_sugar / 4
    sugar_lost = sugar_per_bag / 2
    remaining_sugar = total_sugar - sugar_lost
    result = remaining_sugar
    return result

print(solution())