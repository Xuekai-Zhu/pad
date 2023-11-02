def solution():
    """A garden produced 237 potatoes, 60 fewer cucumbers and twice as many peppers than the cucumbers. How many vegetables did the garden produce?"""
    # Define the number of potatoes
    potatoes = 237

    # Calculate the number of cucumbers
    cucumbers = potatoes - 60

    # Calculate the number of peppers
    peppers = cucumbers * 2

    # Calculate the total number of vegetables
    vegetables = potatoes + cucumbers + peppers

    # return the result
    result = vegetables
    return result

print(solution())