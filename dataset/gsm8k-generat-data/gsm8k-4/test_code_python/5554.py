def solution():
    """Dante needs half as many cups of flour to bake his chocolate cake as he needs eggs. If he uses 60 eggs in his recipe, calculate the total number of cups of flour and eggs that he uses altogether."""
    # Define the ratio of eggs to flour
    eggs_to_flour_ratio = 2

    # Calculate the number of cups of flour needed
    cups_of_flour = 60 / eggs_to_flour_ratio

    # Calculate the total number of eggs and cups of flour used
    total_eggs_and_flour = 60 + cups_of_flour

    # return the result
    result = total_eggs_and_flour
    return result

print(solution())