def solution():
    rent_cost_per_day = 30
    supplies_cost_per_day = 12
    pancake_price = 2

    # Calculate the total cost of expenses per day
    total_expenses_per_day = rent_cost_per_day + supplies_cost_per_day

    # Calculate how much profit Janina makes per pancake
    profit_per_pancake = pancake_price - total_expenses_per_day

    # Calculate how many pancakes Janina must sell each day to cover her expenses
    pancakes_to_sell_per_day = total_expenses_per_day / profit_per_pancake
    result = round(pancakes_to_sell_per_day)  # round to the nearest whole number
    return result

print(solution())