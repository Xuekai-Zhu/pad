def solution():
    """A bottle can hold 2 cups of water. How many cups of water are needed to fill up 10 whole bottles and 5 half-capacity bottles?"""
    # Define the capacity of a bottle
    BOTTLE_CAPACITY = 2

    # Calculate the total number of cups needed for whole bottles
    whole_cups = 10 * BOTTLE_CAPACITY

    # Calculate the total number of cups needed for half-capacity bottles
    half_cups = 5 * BOTTLE_CAPACITY * 0.5

    # Calculate the total number of cups needed
    total_cups = whole_cups + half_cups

    # return the result
    result = total_cups
    return result

print(solution())