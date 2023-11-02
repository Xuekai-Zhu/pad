def solution():
    cost_components = 800
    markup_factor = 1.4
    num_computers = 60
    rent = 5000
    extra_expenses = 3000

    # Calculate the selling price of each computer
    selling_price = cost_components * markup_factor

    # Calculate total revenue from selling 60 computers
    total_revenue = selling_price * num_computers

    # Calculate total expenses
    total_expenses = rent + extra_expenses + (cost_components * num_computers)

    # Calculate profit
    profit = total_revenue - total_expenses
    result = profit
    return result

print(solution())