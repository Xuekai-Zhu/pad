def solution():
    """A baker is making bread according to a recipe that requires him to use 3 eggs for every 2 cups of flour. If the baker wants to use up the 6 cups of flour he has remaining in his pantry, how many eggs will he need to use?"""
    cups_of_flour = 6
    eggs_required = (cups_of_flour / 2) * 3
    result = eggs_required
    return result

print(solution())