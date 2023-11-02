def solution():
    budget = 200  # Harry and Kevin have a budget of $200
    balloon_sheet_cost = 42  # The giant sheet to turn into a balloon costs $42
    rope_cost = 18  # The rope costs $18
    propane_cost = 14  # The propane tank and burner cost $14

    # Calculate the total cost of the materials
    total_cost = balloon_sheet_cost + rope_cost + propane_cost

    # Calculate the budget left for helium
    budget_left = budget - total_cost

    # Calculate the total weight of helium they can buy
    helium_weight = budget_left / 1.5  # Helium costs $1.50 per ounce

    # Calculate the total increase in altitude due to the helium
    altitude_increase = helium_weight * 113  # The balloon can fly 113 feet higher for every ounce of helium

    result = altitude_increase
    return result

print(solution())