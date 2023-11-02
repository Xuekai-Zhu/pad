def solution():
    
    # Define the cost per kilogram of oranges
    ORANGE_COST = 3

    # Define the amount of juice needed per liter
    juice_per_liter = 1

    # Calculate the total amount of oranges needed
    total_oranges = juice_per_liter * 5

    # Calculate the total cost of the oranges
    total_cost = total_oranges * ORANGE_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())