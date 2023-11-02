def solution():
    """A bottle can hold 2 cups of water. How many cups of water are needed to fill up 10 whole bottles and 5 half-capacity bottles?"""
    # Calculate the total number of bottles
    total_bottles = 10 + 5 * 0.5

    # Calculate the total cups of water needed
    total_water = total_bottles * 2

    # Display the total cups of water needed
    result = total_water
    return result

print(solution())