def solution():
    """Harry wants to build a homemade helium balloon with his son, Kevin, so he and Kevin go to the store with $200. They buy a giant sheet to turn into a balloon for $42, a rope for $18, and a propane tank and burner for $14. They plan to use the rest of the money on helium. The helium is $1.50 per ounce. For every ounce they buy, the balloon can fly 113 feet higher. How many feet up can they fly the balloon?"""
    # Define the budget and the cost of materials
    budget = 200
    materials_cost = 42 + 18 + 14

    # Calculate the remaining budget and the amount of helium they can buy
    remaining_budget = budget - materials_cost
    helium_amount = remaining_budget / 1.5

    # Calculate the height the balloon can fly
    height = helium_amount * 113

    # return the result
    result = height
    return result

print(solution())