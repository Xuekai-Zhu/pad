def solution():
    """Jose needs 12 tablespoons of lemon juice to make a dozen of his lemon cupcakes. Every lemon provides 4 tablespoons of lemon juice. If he needs to make 3 dozen cupcakes, how many lemons will he need?"""
    # Define the amount of lemon juice needed per dozen cupcakes
    lemon_juice_per_dozen = 12

    # Calculate the total amount of lemon juice needed for 3 dozen cupcakes
    total_lemon_juice = lemon_juice_per_dozen * 3

    # Calculate the number of lemons needed to provide the required amount of lemon juice
    lemons_needed = total_lemon_juice / 4

    # Round up to the nearest whole number of lemons
    lemons_needed = int(math.ceil(lemons_needed))

    result = lemons_needed
    return result

print(solution())