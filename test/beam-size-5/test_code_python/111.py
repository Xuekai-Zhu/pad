def solution():
    
    # Define the prices of the two x 4 x 10 boards and five 4 x 10 boards
    PRICE_1 = 10
    PRICE_2 = 10
    PRICE_3 = 16

    # Calculate the total cost of the two x 4 x 10 boards
    total_cost = (10 * PRICE_1) + (5 * PRICE_2)

    # Calculate the total revenue from selling the five 4 x 4 x 10 boards
    total_revenue = (10 * PRICE_1) + (5 * PRICE_2)

    # Calculate the profit
    profit = total_revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())