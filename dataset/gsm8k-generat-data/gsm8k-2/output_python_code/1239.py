def solution():
    """
    Harry wants to build a homemade helium balloon with his son, Kevin, so he and Kevin go to the store with $200.
    They buy a giant sheet to turn into a balloon for $42, a rope for $18, and a propane tank and burner for $14.
    They plan to use the rest of the money on helium.
    The helium is $1.50 per ounce. For every ounce they buy, the balloon can fly 113 feet higher.
    How many feet up can they fly the balloon?
    """

    total_money = 200
    sheet_cost = 42
    rope_cost = 18
    propane_cost = 14
    helium_cost_per_ounce = 1.5

    # Calculate the amount of money left for helium after buying the other supplies
    money_left = total_money - sheet_cost - rope_cost - propane_cost

    # Calculate the maximum amount of helium they can buy with the money left
    max_helium_ounces = money_left / helium_cost_per_ounce

    # Calculate the maximum height the balloon can fly
    max_height = max_helium_ounces * 113

    result = max_height
    return result

print(solution())