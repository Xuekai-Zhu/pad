def solution():
    
    # Define the cost of lemons and sugar per gallon
    LEMON_COST = 3
    SUGAR_COST = 2

    # Define the number of glasses per gallon and the profit made
    GLASSES_PER_GALLON = 20
    PROFIT = 25

    # Calculate the total number of glasses sold
    total_glasses = GLASSES_PER_GALLON * 2

    # Calculate the total revenue from selling lemonade
    total_revenue = total_glasses * 0.5

    # Calculate the total cost of lemons and sugar
    total_cost = (PROFIT / 2) * LEMON_COST + SUGAR_COST

    # Calculate the cost of lemons
    lemon_cost = total_revenue - total_cost

    # Display the cost of lemons
    result = lemon_cost
    return result

print(solution())