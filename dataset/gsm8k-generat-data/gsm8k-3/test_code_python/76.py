def solution():
    """A garden produced 237 potatoes, 60 fewer cucumbers and twice as many peppers than the cucumbers. How many vegetables did the garden produce?"""
    # Define the number of potatoes and the difference in the number of cucumbers
    potatoes = 237
    cucumber_diff = 60

    # Calculate the number of cucumbers
    cucumbers = potatoes - cucumber_diff

    # Calculate the number of peppers
    peppers = cucumbers * 2

    # Calculate the total number of vegetables
    total_vegetables = potatoes + cucumbers + peppers

    # Return the result
    result = total_vegetables
    return result

print(solution())