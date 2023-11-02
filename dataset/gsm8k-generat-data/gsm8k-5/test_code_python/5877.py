def solution():
    cost_of_lemons = 10
    cost_of_sugar = 5
    cost_of_cups = 3
    total_expenses = cost_of_lemons + cost_of_sugar + cost_of_cups
    number_of_cups_sold = 21
    price_per_cup = 4
    total_revenue = number_of_cups_sold * price_per_cup
    total_profit = total_revenue - total_expenses
    result = total_profit
    return result

print(solution())