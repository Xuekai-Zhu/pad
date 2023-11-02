def solution():
    # Calculate the total daily expenses of Janina
    daily_expenses = 30 + 12  # rent and supplies cost

    # Calculate the revenue Janina earns from selling one pancake
    pancake_revenue = 2

    # Calculate the number of pancakes Janina must sell to cover her daily expenses
    pancakes_per_day = daily_expenses / pancake_revenue
    result = pancakes_per_day
    return result

print(solution())