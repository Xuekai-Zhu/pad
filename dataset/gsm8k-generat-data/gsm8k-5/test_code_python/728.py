def solution():
    money_available = 2 * 20  # Whitney has two $20 bills
    cost_poster = 2 * 5  # Whitney is buying 2 posters, each costing $5
    cost_notebook = 3 * 4  # Whitney is buying 3 notebooks, each costing $4
    cost_bookmark = 2 * 2  # Whitney is buying 2 bookmarks, each costing $2

    # Calculate the total cost of the purchase
    total_cost = cost_poster + cost_notebook + cost_bookmark

    # Calculate the amount of money Whitney will have left over
    money_left = money_available - total_cost
    result = money_left
    return result

print(solution())