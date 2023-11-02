def solution():
    cost_of_components = 800  # Cost of the parts for each computer
    selling_price = 1.4 * cost_of_components  # Selling price of each computer
    monthly_builds = 60  # Number of computers John can build in a month

    revenue = selling_price * monthly_builds  # Total revenue from selling 60 computers
    total_expenses = 5000 + 3000  # John's total monthly expenses for rent and non-rent expenses
    profit = revenue - total_expenses  # John's monthly profit

    result = profit
    return result

print(solution())