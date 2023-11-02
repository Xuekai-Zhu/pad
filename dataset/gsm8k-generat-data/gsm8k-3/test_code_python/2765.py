def solution():
    """Saturday at the ice cream shop, there were twice as many people who ordered vanilla ice cream as ordered chocolate ice cream.  If 220 people ordered ice cream on Saturday, and 20% of those ordered vanilla ice cream, how many people ordered chocolate ice cream?"""
    # Calculate the total number of people who ordered vanilla ice cream
    total_vanilla = round(0.2 * 220)

    # Double the number of people who ordered vanilla to get the number who ordered chocolate
    total_chocolate = 2 * total_vanilla

    # Subtract the number of people who ordered vanilla from the total to get the number who ordered chocolate
    total_chocolate = 220 - total_vanilla

    # Display the number of people who ordered chocolate ice cream
    result = total_chocolate
    return result

print(solution())