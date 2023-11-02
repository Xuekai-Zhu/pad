def solution():
    """A baker is making bread according to a recipe that requires him to use 3 eggs for every 2 cups of flour.  If the baker wants to use up the 6 cups of flour he has remaining in his pantry, how many eggs will he need to use?"""
    # Define the ratio of eggs to flour in the recipe
    EGGS_PER_FLOUR = 3 / 2

    # Define the amount of flour the baker has remaining in his pantry
    flour_remaining = 6

    # Calculate the number of eggs needed using the ratio of eggs to flour
    eggs_needed = EGGS_PER_FLOUR * flour_remaining

    # Display the number of eggs needed
    result = eggs_needed
    return result

print(solution())