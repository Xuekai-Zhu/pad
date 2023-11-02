def solution():
    """Harry wants to build a homemade helium balloon with his son, Kevin, so he and Kevin go to the store with $200. They buy a giant sheet to turn into a balloon for $42, a rope for $18, and a propane tank and burner for $14. They plan to use the rest of the money on helium. The helium is $1.50 per ounce. For every ounce they buy, the balloon can fly 113 feet higher. How many feet up can they fly the balloon?"""
    # Define the cost of the balloon materials
    BALLOON_SHEET_COST = 42
    ROPE_COST = 18
    PROPANE_COST = 14

    # Calculate the total amount spent on materials
    total_materials_cost = BALLOON_SHEET_COST + ROPE_COST + PROPANE_COST

    # Determine the amount of money left for helium
    helium_budget = 200 - total_materials_cost

    # Calculate the amount of helium they can buy
    helium_ounces = helium_budget / 1.5

    # Determine how many feet up the balloon can fly with the amount of helium they bought
    feet_higher = helium_ounces * 113

    # Display how many feet up the balloon can fly
    result = feet_higher
    return result

print(solution())