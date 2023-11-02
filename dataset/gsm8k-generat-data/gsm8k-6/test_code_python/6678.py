def solution():
    # Calculate the number of orchards for oranges
    orange_orchards = 8 / 2  # oranges occupy half as many orchards as lemons

    # Calculate the number of orchards for limes and grapefruits
    lime_grapefruit_orchards = 16 - 8 - orange_orchards  # remaining orchards are split between limes and grapefruits

    # Calculate the number of orchards for grapefruits
    grapefruit_orchards = lime_grapefruit_orchards / 2  # grapefruits and limes split the remaining orchards equally

    result = grapefruit_orchards
    return result

print(solution())