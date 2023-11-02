def solution():
    """The height of the tree in Kilmer Park is 52 feet. Each year it grows 5 feet. In 8 years, what will the height of the tree be in inches, assuming 1 foot is 12 inches."""
    tree_height = 52
    years_passed = 8
    growth_per_year = 5
    total_growth = growth_per_year * years_passed
    height_in_inches = (tree_height + total_growth) * 12
    result = height_in_inches
    return result

print(solution())