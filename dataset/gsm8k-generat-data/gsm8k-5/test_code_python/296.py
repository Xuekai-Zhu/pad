def solution():
    # Divide the sugar into 4 bags equally
    sugar_per_bag = 24 / 4

    # One of the bags gets torn and half of the sugar falls to the ground
    remaining_sugar = (sugar_per_bag * 3) + (sugar_per_bag / 2)
    result = remaining_sugar
    return result

print(solution())