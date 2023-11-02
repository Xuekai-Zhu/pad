def solution():
    """A baker is making bread according to a recipe that requires him to use 3 eggs for every 2 cups of flour. If the baker wants to use up the 6 cups of flour he has remaining in his pantry, how many eggs will he need to use?"""
    # Define the number of eggs required for 2 cups of flour
    eggs_per_2cups = 3

    # Calculate the number of eggs required for 6 cups of flour
    eggs_required = (6/2) * eggs_per_2cups

    # return the result
    result = eggs_required
    return result

print(solution())