def solution():
    # Calculate the amount earned from the three families
    amount_from_3_families = 10 * 3  # $10 from each of the 3 families

    # Calculate the amount earned from the 15 families
    amount_from_15_families = 5 * 15  # $5 from each of the 15 families

    # Calculate the total amount earned so far
    total_amount_earned = amount_from_3_families + amount_from_15_families

    # Calculate the amount remaining to reach the goal
    goal_amount = 150
    remaining_amount = goal_amount - total_amount_earned
    result = remaining_amount
    return result

print(solution())