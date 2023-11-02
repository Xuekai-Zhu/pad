def solution():
    """Jose needs 12 tablespoons of lemon juice to make a dozen of his lemon cupcakes.  Every lemon provides 4 tablespoons of lemon juice.  If he needs to make 3 dozen cupcakes, how many lemons will he need?"""
    # Define the amount of lemon juice needed per dozen cupcakes
    LEMON_JUICE_PER_DOZEN = 12

    # Define the amount of lemon juice provided by one lemon
    LEMON_JUICE_PER_LEMON = 4

    # Calculate the total amount of lemon juice needed
    total_lemon_juice_needed = LEMON_JUICE_PER_DOZEN * 3

    # Calculate the number of lemons needed
    lemons_needed = total_lemon_juice_needed / LEMON_JUICE_PER_LEMON

    # Display the number of lemons needed
    result = lemons_needed
    return result

print(solution())