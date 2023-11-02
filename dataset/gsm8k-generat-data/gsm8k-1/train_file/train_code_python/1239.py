def solution():
    """Harry wants to build a homemade helium balloon with his son, Kevin, so he and Kevin go to the store with $200. They buy a giant sheet to turn into a balloon for $42, a rope for $18, and a propane tank and burner for $14. They plan to use the rest of the money on helium. The helium is $1.50 per ounce. For every ounce they buy, the balloon can fly 113 feet higher. How many feet up can they fly the balloon?"""
    budget = 200
    total_cost = 42 + 18 + 14  # sheet + rope + propane
    helium_budget = budget - total_cost
    helium_price_per_ounce = 1.5
    helium_total_ounces = helium_budget / helium_price_per_ounce
    additional_height_per_ounce = 113
    total_additional_height = helium_total_ounces * additional_height_per_ounce
    result = total_additional_height
    return result

print(solution())