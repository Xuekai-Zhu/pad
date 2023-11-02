def solution():
    """At the new store, there are 3 times as many grape candies as cherry candies,
        and 2 times as many apple candies as grape candies. All the candies cost $2.50 each.
        If the total cost of the candies is $200, how many grape candies does the store have?"""
    # Define the cost per candy
    CANDY_COST = 2.5

    # Define the number of cherry candies
    cherry_candies = None

    # Define the number of grape candies
    grape_candies = None

    # Define the number of apple candies
    apple_candies = None

    # Define the total cost of the candies
    total_cost = 200

    # Set up the system of equations based on the given information
    # grape candies = 3 * cherry candies
    # apple candies = 2 * grape candies
    # total_cost = cherry_candies * CANDY_COST + grape_candies * CANDY_COST + apple_candies * CANDY_COST
    #
    # Simplifying the equations:
    # grape_candies = 3 * cherry_candies
    # apple_candies = 6 * cherry_candies
    # total_cost = 12 * cherry_candies * CANDY_COST

    # Solve for cherry_candies
    cherry_candies = total_cost / (12 * CANDY_COST)

    # Calculate the number of grape candies
    grape_candies = 3 * cherry_candies

    result = grape_candies
    return result

print(solution())