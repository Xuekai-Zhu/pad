def solution():
    """The height of the tree in Kilmer Park is 52 feet. Each year it grows 5 feet. 
    In 8 years, what will the height of the tree be in inches, assuming 1 foot is 12 inches."""
    initial_height = 52
    growth_rate = 5
    years = 8
    height_in_feet = initial_height + (growth_rate * years)
    height_in_inches = height_in_feet * 12
    result = height_in_inches
    return result

print(solution())