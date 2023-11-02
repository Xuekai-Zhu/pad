def solution():
    """Addilynn went to the grocery store and bought six dozen eggs for use in her house. After two weeks, she used half of the eggs, then accidentally broke 15 of the remaining eggs while moving them to clean the shelves. How many eggs are left on the shelf?"""
    eggs_bought = 6 * 12
    eggs_remaining_after_two_weeks = eggs_bought / 2
    eggs_remaining = eggs_remaining_after_two_weeks - 15
    result = eggs_remaining
    return result

print(solution())