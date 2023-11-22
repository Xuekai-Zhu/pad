def solution():
    
    # Define the number of yogurts eaten per day and the price per yogurt
    YOGURTS_PER_DAY = 2
    PRICE_PER_YOGURT = 5.00

    # Calculate the total number of yogurts eaten over 30 days
    total_yogurts = YOGURTS_PER_DAY * 30

    # Calculate the total cost of the yogurts
    total_cost = total_yogurts * PRICE_PER_YOGURT

    # Display the total cost
    result = total_cost
    return result

print(solution())