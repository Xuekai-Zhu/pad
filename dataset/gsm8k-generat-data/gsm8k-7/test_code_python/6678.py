def solution():
    total_orchards = 16

    # Calculate the number of lemon orchards
    lemon_orchards = 8

    # Calculate the number of orange orchards (half as many as lemons)
    orange_orchards = lemon_orchards / 2

    # Calculate the remaining orchards for limes and grapefruits
    remaining_orchards = total_orchards - lemon_orchards - orange_orchards

    # Calculate the number of orchards for grapefruits (half of the remaining)
    grapefruit_orchards = remaining_orchards / 2
    result = grapefruit_orchards
    return result

print(solution())