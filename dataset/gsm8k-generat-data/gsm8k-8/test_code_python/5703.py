def solution():
    # Calculate the total revenue from the first two customers
    total_revenue_1 = 5 * 4 * 2

    # Calculate the total revenue from the second two customers
    total_revenue_2 = 5 * 2 * 2

    # Calculate the total revenue from all customers
    total_revenue = total_revenue_1 + total_revenue_2

    # Calculate the number of hamburgers Frank still needs to sell
    hamburgers_left = (50 - total_revenue) / 5
    result = hamburgers_left
    return result

print(solution())