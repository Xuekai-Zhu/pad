def solution():
    """Beth went shopping. She bought 15 more cans of peas than twice the number of cans of corn that she bought. If she bought 35 cans of peas, how many cans of corn did she buy?"""
    # Define the variables
    peas = 35
    corn = None

    # Use the given information to set up an equation and solve for corn
    corn = (peas - 15) / 2

    result = corn
    return result

print(solution())