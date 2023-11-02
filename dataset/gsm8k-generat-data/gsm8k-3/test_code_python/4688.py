def solution():
    """Emily bought a shirt and a coat for $600. What does the shirt cost if it is one-third the price of the coat?"""
    # Let's assume the coat costs x dollars
    # Then the shirt costs 1/3 of x dollars
    x = 3 * (600 / 4) # solve for x, knowing that the total cost is $600
    shirt_cost = x / 3 # calculate the cost of the shirt

    # Display the cost of the shirt
    result = shirt_cost
    return result

print(solution())