def solution():
    """Jose needs 12 tablespoons of lemon juice to make a dozen of his lemon cupcakes. Every lemon provides 4 tablespoons of lemon juice. If he needs to make 3 dozen cupcakes, how many lemons will he need?"""
    lemon_juice_per_dozen = 12
    lemons_per_dozen = lemon_juice_per_dozen / 4
    total_cupcakes = 3 * 12
    total_lemons = lemons_per_dozen * total_cupcakes
    result = total_lemons
    return result

print(solution())