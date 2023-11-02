def solution():
    initial_weight = 0
    box_weight = 2  # weight of the box

    # Add jelly beans to bring the weight to 2 pounds
    initial_weight += box_weight
    initial_weight += (2 - initial_weight)

    # Add brownies to triple the weight
    initial_weight *= 3

    # Add 2 pounds of jelly beans
    initial_weight += 2

    # Add gummy worms to double the weight again
    initial_weight = initial_weight * 2

    result = initial_weight
    return result

print(solution())