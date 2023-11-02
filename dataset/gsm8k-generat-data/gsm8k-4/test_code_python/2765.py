def solution():
    """Saturday at the ice cream shop, there were twice as many people who ordered vanilla ice cream as ordered chocolate ice cream.  If 220 people ordered ice cream on Saturday, and 20% of those ordered vanilla ice cream, how many people ordered chocolate ice cream?"""
    # Find the total number of people who ordered vanilla ice cream
    total_vanilla = 0.2 * 220

    # Find the ratio of vanilla to chocolate ice cream
    vanilla_to_chocolate = 2

    # Use the total number of people who ordered vanilla ice cream and the ratio to solve for the number who ordered chocolate
    total_ice_cream = 220
    total_chocolate = total_ice_cream / (vanilla_to_chocolate + 1)

    # Return the result
    result = total_chocolate
    return result

print(solution())