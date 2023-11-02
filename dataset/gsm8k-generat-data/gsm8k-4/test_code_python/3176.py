def solution():
    """Cynthia has three children whose ages add up to 35. Matthew is two years older than Rebecca and four years younger than Freddy. How many years old is Freddy?"""
    # Define the total age of the three children
    total_age = 35

    # Set up the equations for the ages of the three children
    # Let x be Rebecca's age
    # Then Matthew is x + 2 and Freddy is x + 6
    # The sum of their ages is 35, so we get the equation:
    # x + (x + 2) + (x + 6) = 35
    # Solving for x, we get:
    # x = 9
    # Therefore, Freddy's age is x + 6 = 15

    freddy_age = 15
    result = freddy_age
    return result

print(solution())