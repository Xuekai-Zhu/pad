def solution():
    # Calculate total money earned from 3 families
    money_from_3_families = 3 * 10

    # Calculate total money earned from 15 families
    money_from_15_families = 15 * 5

    # Calculate total money earned so far
    total_money_earned = money_from_3_families + money_from_15_families

    # Calculate how much more money they need to reach their goal
    money_needed = 150 - total_money_earned
    result = money_needed
    return result

print(solution())