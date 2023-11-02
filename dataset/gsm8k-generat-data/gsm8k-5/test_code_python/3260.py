def solution():
    # Calculate total spending on lattes for a year
    latte_cost = 4 * 5 * 52  # $4 per latte, 5 days per week, 52 weeks per year

    # Calculate total spending on iced coffee for a year
    iced_coffee_cost = 2 * 3 * 52  # $2 per iced coffee, 3 days per week, 52 weeks per year

    # Calculate total spending for a year
    total_spending = latte_cost + iced_coffee_cost

    # Calculate new goal for total spending
    new_spending_goal = 0.75 * total_spending  # 25% less than current spending

    # Calculate amount saved
    amount_saved = total_spending - new_spending_goal
    result = amount_saved
    return result

print(solution())