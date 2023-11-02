def solution():
    cost_of_lemons = 10
    cost_of_sugar = 5
    cost_of_cups = 3
    price_per_cup = 4
    total_cups_sold = 21

    # Calculate the total cost of all expenses
    total_expenses = cost_of_lemons + cost_of_sugar + cost_of_cups

    # Calculate the total revenue from selling cups of lemonade
    total_revenue = price_per_cup * total_cups_sold

    # Calculate the total profit
    total_profit = total_revenue - total_expenses
    result = total_profit
    return result

print(solution())