def solution():
    
    # Define the cost of each item
    APPLE_PRICE = 5.20
    ORANGE_PRICE = 3.30

    # Define the number of each item purchased
    num_apples = 5
    num_oranges = 5

    # Calculate the total cost of the purchase
    total_cost = (num_apples * APPLE_PRICE) + (num_oranges * ORANGE_PRICE)

    # Display the total cost
    result = total_cost
    return result

print(solution())