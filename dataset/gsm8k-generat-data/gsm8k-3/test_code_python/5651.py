def solution():
    """Nathan bought one large box of bananas. He saw that there are six bunches with eight bananas in a bunch and five bunches with seven bananas in a bunch. How many bananas did Nathan have?"""
    # Calculate the total number of bananas in the bunches with 8 bananas
    bananas_8 = 6 * 8

    # Calculate the total number of bananas in the bunches with 7 bananas
    bananas_7 = 5 * 7

    # Calculate the total number of bananas
    total_bananas = bananas_8 + bananas_7

    # Display the total number of bananas
    result = total_bananas
    return result

print(solution())