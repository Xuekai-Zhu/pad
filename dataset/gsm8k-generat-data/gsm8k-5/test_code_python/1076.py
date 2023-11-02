def solution():
    # Calculate the total cost of the items
    total_cost = (3 * 5) + (2 * 15) + (5 * 4)  # 3 dolls, 2 clocks, and 5 glasses

    # Calculate the profit by subtracting the total cost from the total revenue
    total_revenue = total_cost + 40  # Stella spent $40 to buy everything, so she needs to add this to her revenue
    dolls_revenue = 3 * 5
    clocks_revenue = 2 * 15
    glasses_revenue = 5 * 4
    profit = total_revenue - (dolls_revenue + clocks_revenue + glasses_revenue)

    result = profit
    return result

print(solution())