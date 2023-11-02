def solution():
    """A baker is making bread according to a recipe that requires him to use 3 eggs for every 2 cups of flour. If the baker wants to use up the 6 cups of flour he has remaining in his pantry, how many eggs will he need to use?"""
    cups_of_flour = 6
    eggs_needed = (3/2) * cups_of_flour
    result = eggs_needed
    return result

print(solution())