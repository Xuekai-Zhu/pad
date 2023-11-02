def solution():
    total_budget = 200
    balloon_sheet_cost = 42
    rope_cost = 18
    propane_cost = 14
    remaining_budget = total_budget - balloon_sheet_cost - rope_cost - propane_cost

    helium_cost_per_ounce = 1.5
    height_increase_per_ounce = 113

    # Calculate the total amount of helium they can buy with the remaining budget
    total_helium_ounces = remaining_budget / helium_cost_per_ounce

    # Calculate the total height increase they can achieve with the helium
    total_height_increase = total_helium_ounces * height_increase_per_ounce
    result = total_height_increase
    return result

print(solution())