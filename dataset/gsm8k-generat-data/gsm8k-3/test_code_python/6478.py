def solution():
    """Bob has planted corn in his garden, and it has just started to sprout. A week after planting it, it had grown 2 inches. The next week, its height increased by twice as much as it had the first week. In the third week, it grew 4 times as much as it did the week before. How tall are the corn plants now?"""
    # Define the initial height of the corn plants
    height = 2

    # Calculate the height of the corn plants after the second week
    height += 2 * 2

    # Calculate the height of the corn plants after the third week
    height += 4 * 4

    # Display the final height of the corn plants
    result = height
    return result

print(solution())