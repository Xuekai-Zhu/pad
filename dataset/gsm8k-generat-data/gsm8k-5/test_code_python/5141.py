def solution():
    # Calculate the total cost of the meal before tip
    total_meal_cost = 9 + (2 * 20) + 11  # Appetizer + 2 entrees + dessert

    # Calculate the amount of the tip
    tip_amount = 0.3 * total_meal_cost

    # Calculate the total cost of the meal including tip
    total_cost_with_tip = total_meal_cost + tip_amount
    result = total_cost_with_tip
    return result

print(solution())