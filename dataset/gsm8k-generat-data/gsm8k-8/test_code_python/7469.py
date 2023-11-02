def solution():
    # Calculate the total cost of making 12 bracelets
    total_cost = 12 * 1

    # Calculate the total revenue from selling 12 bracelets
    total_revenue = 12 * 1.5

    # Calculate Josh's profit
    profit = total_revenue - total_cost

    # Subtract the cost of the cookies and find the price of the box of cookies
    box_of_cookies_cost = 3 - profit
    result = box_of_cookies_cost
    return result

print(solution())