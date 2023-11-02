def solution():
    """Jose needs 12 tablespoons of lemon juice to make a dozen of his lemon cupcakes. Every lemon provides 4 tablespoons of lemon juice.
    If he needs to make 3 dozen cupcakes, how many lemons will he need?"""
    lemon_juice_per_cupcake = 1
    tablespoons_per_lemon = 4
    cupcakes_needed = 3 * 12
    lemons_needed = (cupcakes_needed * lemon_juice_per_cupcake) / tablespoons_per_lemon
    result = lemons_needed
    return result

print(solution())