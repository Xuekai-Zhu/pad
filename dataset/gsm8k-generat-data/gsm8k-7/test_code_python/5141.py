def solution():
    appetizer_cost = 9.0
    entree_cost = 20.0
    dessert_cost = 11.0
    tip_percent = 0.3  # 30% tip

    # Calculate the total cost of the meal without the tip
    total_cost = appetizer_cost + (2 * entree_cost) + dessert_cost

    # Calculate the amount of the tip
    tip_amount = total_cost * tip_percent

    # Calculate the total cost of the meal with the tip
    total_cost_with_tip = total_cost + tip_amount
    result = total_cost_with_tip
    return result

print(solution())