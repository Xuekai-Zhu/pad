def solution():
    """Nathan bought one large box of bananas. He saw that there are six bunches with eight bananas in a bunch and five bunches with seven bananas in a bunch. How many bananas did Nathan have?"""
    # Calculate the number of bananas in the bunches with 8 bananas
    bananas_in_eight_bunches = 6 * 8

    # Calculate the number of bananas in the bunches with 7 bananas
    bananas_in_seven_bunches = 5 * 7

    # Calculate the total number of bananas Nathan has
    total_bananas = bananas_in_eight_bunches + bananas_in_seven_bunches

    result = total_bananas
    return result

print(solution())