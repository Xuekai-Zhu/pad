def solution():
    initial_weight = 0
    jellybean_weight = 1/2   # 2 pounds/4 = 0.5 pounds
    brownie_weight = 1.5   # triple the weight of the box after adding the jelly beans
    gummy_worm_weight = 3   # double the weight of the box after adding the brownies

    # Add jelly beans to bring the weight of the box to 2 pounds
    initial_weight += jellybean_weight

    # Add brownies to triple the weight of the box
    initial_weight *= 3

    # Add another 2 pounds of jelly beans
    initial_weight += (2 * jellybean_weight)

    # Add gummy worms to double the weight of the box
    initial_weight *= 2

    result = initial_weight
    return result

print(solution())