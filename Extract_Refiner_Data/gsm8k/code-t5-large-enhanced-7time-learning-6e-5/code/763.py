def solution():
    
    # Define the cost per kilogram of oranges and the amount of juice needed to make 1 liter of juice
    COST_PER_KG = 3
    AMOUNT_PER_LITER = 1

    # Calculate the total amount of oranges needed to make 4 liters of juice
    total_oranges = 4 * AMOUNT_PER_LITER

    # Calculate the total cost of the oranges
    total_cost = total_oranges * COST_PER_KG

    # Display the total cost
    result = total_cost
    return result

print(solution())