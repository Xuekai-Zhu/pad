def solution():
    """At the new store, there are 3 times as many grape candies as cherry candies, and 2 times as many apple candies as grape candies.
    All the candies cost $2.50 each. If the total cost of the candies is $200, how many grape candies does the store have?"""
    # Define the cost of each candy
    COST_PER_CANDY = 2.5

    # Define the ratio of grape:candy
    GRAPE_TO_CHERRY = 3
    APPLE_TO_GRAPE = 2

    # Calculate the total cost
    total_cost = 200

    # Calculate the total number of candies
    total_candies = int(total_cost / COST_PER_CANDY)

    # Calculate the number of cherry candies
    cherry_candies = total_candies / (GRAPE_TO_CHERRY * APPLE_TO_GRAPE + GRAPE_TO_CHERRY + 1)

    # Calculate the number of grape candies
    grape_candies = GRAPE_TO_CHERRY * cherry_candies

    # Display the number of grape candies
    result = grape_candies
    return result

print(solution())