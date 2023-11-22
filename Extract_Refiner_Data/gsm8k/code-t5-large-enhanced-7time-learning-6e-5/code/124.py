def solution():
    
    # Define the cost of each pepper
    PEPPER_PRICE = 15

    # Calculate the cost of each watermelon
    watermelon_cost = 3 * PEPPER_PRICE

    # Calculate the cost of each orange
    orange_cost = watermelon_cost - 5

    # Calculate the total cost of the purchase
    total_cost = 4 * watermelon_cost + 20 * PEPPER_PRICE + 10 * orange_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())